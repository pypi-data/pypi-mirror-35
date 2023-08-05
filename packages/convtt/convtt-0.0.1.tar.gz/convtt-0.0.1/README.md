## publish bidcap

**build the package**

```bash
python bidcap/setup.py sdist bdist_wheel
```

**publish on test pypi**
```bash
# upload package
twine upload --repository-url https://test.pypi.org/legacy/ dist/bidcap-0.0.1*
# install package
python -m pip install --index-url https://test.pypi.org/simple/ bidcap
```

**publish on live pypi**
```bash
# upload package
twine upload dist/bidcap-0.0.1*
 # install package
python -m pip install bidcap
```

## publish cudam

**build the package**

```bash
python cudam/setup.py sdist bdist_wheel
```

**publish on test pypi**
```bash
# upload package
twine upload --repository-url https://test.pypi.org/legacy/ dist/cudam-0.0.4*
# install package
python -m pip install --index-url https://test.pypi.org/simple/ cudam
```

**publish on live pypi**
```bash
# upload package
twine upload dist/cudam-0.0.4*
 # install package
python -m pip install cudam
```

## publish convtt

**build the package**

```bash
python convtt/setup.py sdist bdist_wheel
```

**publish on test pypi**
```bash
# upload package
twine upload --repository-url https://test.pypi.org/legacy/ dist/convtt-0.0.1*
# install package
python -m pip install --index-url https://test.pypi.org/simple/ convtt
```

**publish on live pypi**
```bash
# upload package
twine upload dist/convtt-0.0.1*
 # install package
python -m pip install convtt