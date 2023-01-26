# menu_api

CRUD operations to menu

### http://localhost:8000/menus/{num}/submenus/{num}/dishes/{num}
```shell
http://localhost:8000/menus - Menu list
```
```shell
http://localhost:8000/menus/2 - menu id 2
```
```shell
http://localhost:8000/menus/{num}/submenus - Submenu list
```
```shell
http://localhost:8000/menus/2/submenus/3 - Submenu id 3 in menu 2
```
```shell
http://localhost:8000/menus/{num}/submenus/{num}/dishes/ - Dishes list
```
```shell
http://localhost:8000/menus/2/submenus/3/dishes/4 - Dish 4, submenu id 3, menu 2
```
## Launch
```shell
uvicorn main:app --reload
```
