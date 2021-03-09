# django-json-field-schema-validator
[![Build Status](https://travis-ci.com/wblxyxolbkhv/django-json-schema-validator.svg?branch=main)](https://travis-ci.com/wblxyxolbkhv/django-json-schema-validator)
[![Coverage Status](https://coveralls.io/repos/github/wblxyxolbkhv/django-json-field-schema-validator/badge.svg?branch=main)](https://coveralls.io/github/wblxyxolbkhv/django-json-field-schema-validator?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Tiny tool for Django JSONField validation through [JSON Schema](https://python-jsonschema.readthedocs.io/en/latest/validate/)
## Installation

```shell script
pip install django-json-field-schema-validator
```

## Example

```python
from django.db import models
from django_json_field_schema_validator.validators import JSONFieldSchemaValidator

schema = {
    '$schema': f'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'foo': {'type': 'number'},
        'bar': {'type': 'string'}
    },
    'required': ['foo', 'bar']
}

class SomeMode(models.Model):
    some_field = models.JSONField(validators=[JSONFieldSchemaValidator(schema)])

```
