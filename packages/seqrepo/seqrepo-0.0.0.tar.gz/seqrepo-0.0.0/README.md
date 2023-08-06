biocommons.seqrepo was formerly called seqrepo.  This package provides
a bridge back to the old name.  It does not provide any functionality
under the seqrepo name.

Steps:

```
pyvenv venv
source venv/bin/activate
pip install wheel
python setup.py sdist bdist bdist_egg bdist_wheel upload
```

