# menu_api

 Api полностью рабочее, валидацию изначально сделал тайп-хинтами, поэтому в постмане проверку на null проходит с 422 кодом. Подключение к Postgre через SqlAlchemy, настройка в файле database.py

## Запуск
```shell
uvicorn main:app --reload
```
