# am4894airflowutils

https://packaging.python.org/en/latest/tutorials/packaging-projects/

```bash
# build dist
py -m build
```

```bash
# upload to testpypi
py -m twine upload --repository testpypi dist/*
```

```bash
# upload to pypi
py -m twine upload --repository pypi dist/*
```

```bash
# install dev requirements
pip install -r .\requirements-dev.txt
```

```bash
# run pytest
pytest
```
