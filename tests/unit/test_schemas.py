import pytest

import schemas
from tests.conftest import testing_urls, urls_with_error


@pytest.mark.parametrize('test_input, expected_result', testing_urls)
def test_url_converted_in_model_url(test_input, expected_result):
    url_model = schemas.Url(url=test_input)
    assert type(url_model) == schemas.Url
    assert url_model.url == expected_result


def test_model_url_type_is_correct():
    url_model = schemas.Url(url='http://test.test')
    assert type(url_model) == schemas.Url


@pytest.mark.parametrize('incorrect_url', urls_with_error)
def test_url_converted_in_model_url(incorrect_url):
    with pytest.raises(ValueError):
        schemas.Url(url=incorrect_url)
