# ckanext-file_uploader_ui

Enhance the [CKAN]() file uploading UI with the following features:

* Upload multiple files at once
* Drag & Drop files

Minimal supported CKAN version: 2.8.1

## Installation

* Activate your CKAN virtual environment
* Install the ckanext-file_uploader_ui package into your virtual environment:
  * `pip install ckanext-file_uploader_ui`
* Add ``file_uploader_ui`` to the ``ckan.plugins`` setting in your CKAN
* Restart CKAN.

## Updating the package on PYPI

Update the version in `VERSION.txt`, then build and upload:

```
rm -rf dist &&\
python setup.py sdist &&\
twine upload dist/*
```

ckanext-file_uploader_ui should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-file_uploader_ui. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

* Create a source distribution of the project
  * `python setup.py sdist`
* Upload the source distribution to PyPI
  * `python setup.py sdist upload`

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-file_uploader_ui
----------------------------------------

ckanext-file_uploader_ui is availabe on PyPI as https://pypi.python.org/pypi/ckanext-file_uploader_ui.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
