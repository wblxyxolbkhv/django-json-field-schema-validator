from setuptools import setup, find_packages     # type: ignore
from os import path

base_dir = path.abspath(path.dirname(__file__))

__version__ = '0.0.2'

# Get the long description from the README file
with open(path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-json-field-schema-validator',
    version=__version__,
    description='Tiny tool for Django JSONField validation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wblxyxolbkhv/django-json-field-schema-validator',
    author='Alexey Nikitenko (wblxyxolbkhv)',
    author_email='alexey.nikitenko1927@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords='django json field schema validator tools',
    packages=find_packages(),
    python_requires='>=3.5, <4',
    install_requires=[
        'Django>=1.0',
        'jsonschema>=3.0.0',
    ],
    project_urls={
        'Source': 'https://github.com/wblxyxolbkhv/django-json-field-schema-validator',   # noqa: E501
    },
)
