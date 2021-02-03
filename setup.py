from setuptools import setup, find_packages     # type: ignore
from os import path

base_dir = path.abspath(path.dirname(__file__))

__version__ = '0.0.1'

# Get the long description from the README file
with open(path.join(base_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-json-schema-validator',
    version=__version__,
    description='Tiny tool for Django JSONField validation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wblxyxolbkhv/django-json-schema-validator',
    author='Alexey Nikitenko (wblxyxolbkhv)',
    author_email='alexey.nikitenko1927@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='django json schema validator',
    packages=find_packages(where='django-json-schema-validator'),
    python_requires='>=3.5, <4',
    install_requires=[
        'Django>=1.0',
        'jsonschema>=3.0.0',
    ],
    project_urls={
        'Source': 'https://github.com/wblxyxolbkhv/django-json-schema-validator',   # noqa: E501
    },
)
