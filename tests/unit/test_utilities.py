import pytest

import utilities
from tests.conftest import testing_urls, urls_with_error


@pytest.mark.parametrize('test_input, expected_result', testing_urls)
def test_prepare_url(test_input, expected_result):
    assert utilities.prepare_url(test_input) == expected_result


@pytest.mark.parametrize('incorrect_url', urls_with_error)
def test_value_error_in_url(incorrect_url):
    with pytest.raises(ValueError):
        utilities.prepare_url(incorrect_url)
