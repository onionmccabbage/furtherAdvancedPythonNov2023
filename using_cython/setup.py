from setuptools import setup
# we may need to pip install
from Cython.Build import cythonize

setup(
    # really only worthwhile for very large Python projects
    ext_modules=cythonize('sample.pyx')
)