import setuptools
from distutils.core import setup

setup(
    name='jinja2-dev-server',
    version="0.0.5b8",
    author="Eamonn Nugent",
    author_email="eamonn.nugent@demilletech.net",
    packages=['jinja2_dev_server'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': ['jinja2-dev-server=jinja2_dev_server.command_line:main'],
    }
)
