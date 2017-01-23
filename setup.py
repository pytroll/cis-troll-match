import setuptools
from trollmatch import version

setuptools.setup(name='trollmatch',
                 version=version.__version__,
                 description='Python package for matching spatial observations',
                 long_description=open('README.md').read().strip(),
                 author=open('AUTHORS').read().strip(),
                 author_email='itkin.m@gmail.com',
                 url='https://pytroll.org',
                 py_modules=['trollmatch'],
                 install_requires=[],
                 license='Lesser GPL v3.0',
                 zip_safe=False,
                 keywords='satellite observations gis measurements matchups',
                 classifiers=['Packages'])
