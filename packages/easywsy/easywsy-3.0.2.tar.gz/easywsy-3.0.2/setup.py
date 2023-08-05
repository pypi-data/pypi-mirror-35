# -*- coding: utf-8 -*-
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='easywsy',
    version='3.0.2',
    description='Simple Web Service development API based on suds',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.e-mips.com.ar/infra/easywsy',
    author='Martín Nicolás Cuesta',
    author_email='cuesta.martin.n@hotmail.com',
    packages=['easywsy', 'easywsy.api', 'easywsy.ws',
              'easywsy.error', 'easywsy.check'],
    license='AGPL3+',
    python_requires='>=3.5',
    install_requires=[
        'suds-py3',
    ],
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
