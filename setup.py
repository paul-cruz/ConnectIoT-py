import pathlib
from setuptools import find_packages, setup

cwd = pathlib.Path(__file__).parent

VERSION = '1.0.0'
PACKAGE_NAME = 'ConnectIoT'
AUTHOR = 'Paul Cruz'
AUTHOR_EMAIL = 'paul.cruz@mexbalia.mx'
URL = 'https://github.com/paul-cruz/ConnectIoT-py'

LICENSE = 'GPL-3.0 license'
DESCRIPTION = 'Library to Connect Python scripts with the ConnectIoT project in the NEAR Protocol Blockchain'
LONG_DESCRIPTION = (cwd / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'requests'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
