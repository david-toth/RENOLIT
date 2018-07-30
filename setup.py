from distutils.core import setup
from Cython.Build import cythonize

setup(name='QCAnalysis',
		version='0.1',
		author='David Toth',
	ext_modules=cythonize("QCAnalysis.pyx")
)
