# menu_api

CRUD operations to menu


## Launch
```shell
uvicorn main:app --reload
```



## urls
Menu list
```shell
http://localhost:8000/menus
```
menu id 2
```shell
http://localhost:8000/menus/2
```
Submenu list

http://localhost:8000/menus/{num}/submenus

Submenu id 3 in menu 2
```shell
http://localhost:8000/menus/2/submenus/3
```
Dishes list

http://localhost:8000/menus/{num}/submenus/{num}/dishes/

Dish 4, submenu id 3, menu 2
```shell
http://localhost:8000/menus/2/submenus/3/dishes/4
```

