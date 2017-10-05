import setuptools
from ctmatch import version

setuptools.setup(name='ctmatch',
                 version=version.__version__,
                 description='Python package for matching spatial observations',
                 long_description=open('README.md').read().strip(),
                 author=open('AUTHORS').read().strip(),
                 author_email='itkin.m@gmail.com',
                 url='https://pytroll.org',
                 py_modules=['ctmatch'],

                 install_requires=['satpy',
                                   'cis',
                                   'numpy',
                                   'trollsched'],

                 license='Lesser GPL v3.0',
                 zip_safe=False,
                 keywords='satellite observations gis measurements matchups',
                 classifiers=['Packages'])
