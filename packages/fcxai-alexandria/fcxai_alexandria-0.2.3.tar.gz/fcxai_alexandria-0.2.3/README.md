# AlexandrIA Libs

Everything for building and remodeling (your application) in one place

Published to PyPI at:
https://pypi.org/project/fcxai-alexandria/

## Installation

```bash
# production
pip install fcxai-alexandria

# development
pip install -e .[dev]
```

## Usage

```python
import alexandria as alx
# alx.awslib
# alx.galib
# alx.s3lib

```

## Publish

```bash
# install publish dependencies
pip install --upgrade build twine
# build
python -m build
# upload
python -m twine upload dist/*
# use your pypi username and password
```
