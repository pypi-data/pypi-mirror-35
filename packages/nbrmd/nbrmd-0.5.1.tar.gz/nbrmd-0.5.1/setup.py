from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='nbrmd',
    version='0.5.1',
    author='Marc Wouts',
    author_email='marc.wouts@gmail.com',
    description='Jupyter from/to R markdown notebooks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mwouts/nbrmd',
    packages=find_packages(),
    entry_points={'console_scripts': ['nbrmd = nbrmd.cli:nbrmd',
                                      'nbsrc = nbrmd.cli:nbsrc'],
                  'nbconvert.exporters':
                      ['rmarkdown = nbrmd:RMarkdownExporter',
                       'pynotebook = nbrmd:PyNotebookExporter',
                       'rnotebook = nbrmd:RNotebookExporter']},
    tests_require=['pytest', 'testfixtures'],
    install_requires=['nbformat>=4.0.0', 'mock', 'pyyaml', 'six'],
    license='MIT',
    classifiers=('Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Framework :: Jupyter',
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python',
                 'Topic :: Text Processing :: Markup',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6')
)
