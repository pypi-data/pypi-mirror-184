import itertools as it
from typing import List
from typing import Union
from warnings import warn

import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Filter
from google.analytics.data_v1beta.types import FilterExpression
from google.analytics.data_v1beta.types import FilterExpressionList
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

from alexandria.galib.utils import get_dates


def ua_to_df(response):
    if type(response) is list:
        return pd.concat(list(map(ua_to_df, response)), ignore_index=True)

    reports = response["reports"][0]

    if "rows" not in reports["data"].keys():
        return pd.DataFrame()

    columnHeader = reports["columnHeader"]["dimensions"]
    metricHeader = reports["columnHeader"]["metricHeader"]["metricHeaderEntries"]
    metricHeader = list(map(lambda x: x["name"], metricHeader))

    columns = columnHeader + metricHeader
    columns = list(map(lambda x: x.replace("ga:", ""), columns))

    data = pd.json_normalize(reports["data"]["rows"])
    data_dimensions = pd.DataFrame(data["dimensions"].tolist())
    data_metrics = pd.DataFrame(data["metrics"].tolist())
    data_metrics = data_metrics.applymap(lambda x: x["values"])
    data_metrics = pd.DataFrame(data_metrics[0].tolist())
    result = pd.concat([data_dimensions, data_metrics], axis=1, ignore_index=True)
    result.columns = columns
    return result


def ua_report(
    start_date,
    end_date,
    view_id,
    dimensions,
    metrics,
    filters,
    service_account,
    scope,
    verbose=False,
):
    """Queries the Analytics Reporting API V4."""
    # auth
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        service_account, scope
    )
    analytics = build("analyticsreporting", "v4", credentials=credentials)

    # fetch results
    responses = []

    next_page_token = ""
    for x in it.count(0, 1):
        if verbose:
            print(
                f"=> Fetching batch [{x}]"
                + ("" if not len(next_page_token) else f", offset by {next_page_token}")
            )

        batch = (
            analytics.reports()
            .batchGet(
                body={
                    "reportRequests": [
                        {
                            "viewId": view_id,
                            "dateRanges": [
                                {"startDate": start_date, "endDate": end_date}
                            ],
                            "dimensions": [{"name": dim} for dim in dimensions],
                            "metrics": [{"expression": metric} for metric in metrics],
                            "filtersExpression": ";".join(filters)
                            if filters is not None
                            else "",
                            "samplingLevel": "LARGE",
                            "pageSize": 100_000,
                            "pageToken": next_page_token,
                        }
                    ]
                }
            )
            .execute()
        )

        responses.append(batch)
        next_page_token = batch["reports"][0].get("nextPageToken", "")

        if next_page_token == "":
            break

    return responses


def ga4_to_df(response):
    if type(response) is list:
        return pd.concat(list(map(ga4_to_df, response)), ignore_index=True)

    num_dims = len(response.dimension_headers)
    num_metrics = len(response.metric_headers)

    data = []
    for row in response.rows:
        dims = {
            response.dimension_headers[i].name: row.dimension_values[i].value
            for i in range(num_dims)
        }
        mtrs = {
            response.metric_headers[i].name: row.metric_values[i].value
            for i in range(num_metrics)
        }
        data.append(dims | mtrs)

    df = pd.DataFrame(data)
    return df


def ga4_report(
    start: str,
    end: str,
    dimensions: List[str],
    metrics: List[str],
    filters: Union[List[str], None],
    property_id,
    service_account: dict,
    verbose: bool = False,
):
    client = BetaAnalyticsDataClient.from_service_account_info(service_account)

    responses = []

    if filters is not None:
        filters = FilterExpression(
            and_group=FilterExpressionList(
                expressions=[
                    FilterExpression(
                        filter=Filter(
                            field_name=filter.split("=")[0],
                            string_filter=Filter.StringFilter(
                                match_type=Filter.StringFilter.MatchType.EXACT,
                                value=filter.split("=")[1],
                            ),
                        )
                    )
                    for filter in filters
                ]
            )
        )
    offset = 0
    for x in it.count(0, 1):
        if verbose:
            print(
                f"=> Fetching batch [{x}]"
                + ("" if not offset else f", offset by {offset}")
            )
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name=dim) for dim in dimensions],
            metrics=[Metric(name=metric) for metric in metrics],
            dimension_filter=filters,
            date_ranges=[DateRange(start_date=start, end_date=end)],
            limit=100000,
            offset=x * 100000,
        )

        response = client.run_report(request)
        responses.append(response)

        # note: the row count might be exactly 100k and be the last batch, in which
        # case the request above will be run again but not return any rows.
        # in this situation, a response object with no associated rows will be added
        # to the list of responses.
        # `ga4_to_df` creates an empty df out of this response and pd.concat does not
        # break when trying to concat with an empty dataframe.
        if response.row_count < 100000:
            break

    # google.analytics.data_v1beta.types.analytics_data_api.RunReportResponse
    # https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/RunReportResponse
    return responses


def load_from_range_date(
    start_date,
    end_date,
    view_id,
    dimensions,
    metrics,
    filters,
    service_account,
    scope,
    verbose=False,
):
    warn(
        "load_from_range_date is deprecated. Use load_from_range_date_ga4 instead",
        DeprecationWarning,
    )

    dates = get_dates(start_date, end_date)
    dfs = []

    for start, end in dates:
        report = ua_report(
            start,
            end,
            view_id=view_id,
            dimensions=dimensions,
            metrics=metrics,
            filters=filters,
            service_account=service_account,
            scope=scope,
            verbose=verbose,
        )
        df = ua_to_df(report)
        dfs.append(df)
    return pd.concat(dfs)


def load_from_range_date_ga4(
    start_date: str,
    end_date: str,
    property_id: str,
    dimensions: List[str],
    metrics: List[str],
    filters: Union[List[str], None],
    service_account: dict,
    verbose: bool = False,
):
    dates = get_dates(start_date, end_date)
    dfs = []

    for start, end in dates:
        report = ga4_report(
            start,
            end,
            property_id=property_id,
            dimensions=dimensions,
            metrics=metrics,
            filters=filters,
            service_account=service_account,
            verbose=verbose,
        )
        df = ga4_to_df(report)
        dfs.append(df)
    return pd.concat(dfs)
