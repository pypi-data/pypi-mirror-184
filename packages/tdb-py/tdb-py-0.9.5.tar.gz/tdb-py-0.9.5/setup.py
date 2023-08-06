import pathlib
import re

import setuptools

ROOT = pathlib.Path(__file__).parent

README = (ROOT / 'README.md').read_text()
INIT = (ROOT / 'tdb.py').read_text()
match = re.search(r"__version__\s*=\s*'(?P<version>.*?)'", INIT)
VERSION = match.group('version')

setuptools.setup(
    name='tdb-py',
    version=VERSION,
    author='Mark Summerfield',
    author_email='mark@qtrac.eu',
    description='A pure Python library supporting Tdb “Text DataBase” ' +
    'format, a plain text human readable typed database storage format ' +
    'superior to CSV.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/mark-summerfield/tdb-py',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'],
    package_dir={'': '.'},
    py_modules=['tdb'],
    python_requires='>=3.8',
    install_requires=['editabletuple'])
