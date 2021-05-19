from typing import List, Iterable

from django.core.exceptions import ValidationError
import jsonschema
from django.utils.deconstruct import deconstructible


@deconstructible
class JSONFieldSchemaValidator:
    def __init__(self, schema: dict, draft_version=7):
        self.schema = schema

        self.draft_version = draft_version
        assert self.draft_version in (3, 4, 6, 7)

        if self.draft_version == 3:
            self.schema_validator_class = jsonschema.Draft3Validator
        elif self.draft_version == 4:
            self.schema_validator_class = jsonschema.Draft4Validator
        elif self.draft_version == 6:
            self.schema_validator_class = jsonschema.Draft6Validator
        elif self.draft_version == 7:
            self.schema_validator_class = jsonschema.Draft7Validator

    def __call__(self, value):
        errors = self.schema_validator_class(self.schema).iter_errors(value)

        django_errors = []
        self._extract_errors(errors, django_errors)
        if django_errors:
            raise ValidationError(django_errors)

        return value

    def __eq__(self, other):
        if not hasattr(other, 'deconstruct'):
            return False
        return self.deconstruct() == other.deconstruct()

    def _extract_errors(
        self,
        errors: Iterable[jsonschema.ValidationError],
        container: List[ValidationError],
    ):
        for error in errors:
            if error.context:
                return self._extract_errors(error.context, container)

            message = str(error).replace("\n\n", ": ").replace("\n", "")
            container.append(ValidationError(message))
