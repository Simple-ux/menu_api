# menu_api

CRUD operations to menu
```shell
### http://localhost:8000/menus/{num}/submenus/{num}/dishes/{num}
```
http://localhost:8000/menus - Menu list

http://localhost:8000/menus/2 - menu id 2

http://localhost:8000/menus/{num}/submenus - Submenu list

http://localhost:8000/menus/2/submenus/3 - Submenu id 3 in menu 2

http://localhost:8000/menus/{num}/submenus/{num}/dishes/ - Dishes list

http://localhost:8000/menus/2/submenus/3/dishes/4 - Dish 4, submenu id 3, menu 2

## Launch
```shell
uvicorn main:app --reload
```
