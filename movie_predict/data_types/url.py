from typing import Any, Self

from urlx import Url as UrlBase


class Url(UrlBase):

    class Config:
        json_encoders = {
            UrlBase: str,
        }

    @classmethod
    def validate(cls, value: Any) -> Self:
        if not isinstance(value, str):
            raise TypeError('string required')
        try:
            return cls.parse(value)
        except (ValueError, IndexError):
            raise ValueError('invalid url format')

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema: dict):
        field_schema.update(
            examples=['https://localhost/api:8000'],
        )
