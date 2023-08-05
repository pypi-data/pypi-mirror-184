import io
import os
from setuptools import setup, find_packages

__version__ = '0.1.13'

setup(
    author="Oleg Matskiv",
    author_email="alpaca00tuha@gmail.com",
    name="pytest-summary",
    version=__version__,
    description="A pytest plugin to send a report and printing summary of tests.",
    long_description=io.open(
        os.path.join(os.path.dirname('__file__'), 'README.md'),
        encoding='utf-8'
    ).read(),
    long_description_content_type='text/markdown',
    license="MIT",
    include_package_data=True,
    packages=find_packages(include=['pytest_summary']),
    requires=["pytest"],
    keywords=['pytest', 'py.test'],
    url="https://github.com/Alpaca00/pytest-summary",
    entry_points={
        'pytest11': [
            'pytest-summary = pytest_summary.plugin',
        ]
    }
)
