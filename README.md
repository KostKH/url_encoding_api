# url_encoding_api

`url_encoding_api` - это API для кодирования url-адреса.

Вы отправляете на эндпойнт `/encode` данного API POST-запрос, с url, который надо закодировать, и в ответ вам возвращается закодированный url.

Документацию по API можно посмотреть по эндпойнтам `/redoc` или `/docs`.

## Системные требования
- Python 3.11+
- Works on Linux, Windows, macOS

## Технологии:
- Python 3.11
- FastAPI
- uvicorn
- pytest

## Как запустить проект:

Необходимо выполнить следующие шаги:
- Склонируйте репозиторий с GitHub:
```
git clone git@github.com:KostKH/url_encoding_api.git
cd url_encoding_api
```
- Создайте и активируйте виртуальное окружение, установите зависимости:
```
python -m venv venv

source venv/bin/activate <<< используйте эту команду, если у вас Linux
source venv/scripts/activate <<< используйте эту команду, если у вас Windows

pip install -r requirements.txt
```
- Запустите приложение:
```
uvicorn main:app
```
После запуска API будет доступно по адресу: `http://<host address>:8000/encode`

## О программе:

Автор: Константин Харьков
