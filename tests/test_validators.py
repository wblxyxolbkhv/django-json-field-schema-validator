import pytest
from django.core.exceptions import ValidationError

from django_json_field_schema_validator.validators import (
    JSONFieldSchemaValidator,
)


@pytest.mark.parametrize("draft_version", (3, 4, 6, 7))
def test_validation_without_errors(draft_version):
    schema = {
        "$schema": f"http://json-schema.org/draft-{draft_version:02d}/schema#",
        "type": "object",
        "properties": {"id": {"type": "number"}, "name": {"type": "string"}},
        "required": ["id", "name"],
    }
    validator = JSONFieldSchemaValidator(schema, draft_version)
    validator({"id": 1, "name": "Foo"})


def test_validation_with_errors():
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {"id": {"type": "number"}, "name": {"type": "string"}},
        "required": ["id", "name"],
    }
    validator = JSONFieldSchemaValidator(schema)
    with pytest.raises(ValidationError):
        validator({"id": 1})


def test_validation_with_context():
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "items": {
                "anyOf": [
                    {"type": "string", "maxLength": 2},
                    {"type": "integer", "minimum": 5},
                ]
            }
        },
        "required": ["items"],
    }
    validator = JSONFieldSchemaValidator(schema)
    with pytest.raises(ValidationError):
        validator({"items": [{}, 3, "foo"]})
