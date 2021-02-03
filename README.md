# django-json-schema-validator

Tiny tool for Django JSONField validation through [JSON Schema](https://python-jsonschema.readthedocs.io/en/latest/validate/)

## Installation
```shell script
pip install django-json-schema-validator
```
## Example

```python
from django.db import models
from django_json_schema_validator.validators import JSONFieldSchemaValidator

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