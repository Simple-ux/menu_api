# menu_api

CRUD operations to menu


## Launch
```shell
uvicorn main:app --reload
```



## urls
### Menu list
```shell
http://localhost:8000/menus
```




### Submenu list
```shell
http://localhost:8000/menus/{num}/submenus
```




### Dishes list
```shell
http://localhost:8000/menus/{num}/submenus/{num}/dishes/
```



Example:
http://localhost:8000/menus/2 - menu id 2
http://localhost:8000/menus/2/submenus/3 - Submenu id 3 in menu 2
http://localhost:8000/menus/2/submenus/3/dishes/4 - Dish 4, submenu id 3, menu 2
