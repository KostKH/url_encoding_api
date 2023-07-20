from urllib.parse import urlunparse

from urllib3.exceptions import LocationParseError
from urllib3.util import parse_url


def prepare_url(url):
    try:
        scheme, auth, host, port, path, query, fragment = parse_url(url)
    except LocationParseError:
        raise ValueError(f'Некорректный URL {url}')

    if not scheme:
        raise ValueError(f'Некорректный URL {url}: Не указана схема, '
                         'либо схема содержит недопустимые символы.')

    if not host:
        raise ValueError(f'Некорректный URL {url}: нет хоста, '
                         'либо слишком много слэшей перед хостом.')

    netloc = auth or ''
    if netloc:
        netloc += '@'
    netloc += host
    if port:
        netloc += f':{port}'

    if not path:
        path = '/'
    return urlunparse([scheme, netloc, path, None, query, fragment])
