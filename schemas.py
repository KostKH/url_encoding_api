from pydantic import BaseModel, field_validator

from utilities import prepare_url


class Url(BaseModel):
    """Схема эндпойнта получения  url на кодирование."""

    url: str

    @field_validator('url')
    def check_convert_url(cls, raw_url):
        return prepare_url(raw_url)
