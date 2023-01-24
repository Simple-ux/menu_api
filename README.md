# menu_api

CRUD operations to menu

### http://localhost:8000/menus/{num}/submenus/{num}/dishes/{num}

http://localhost:8000/menus - список меню

http://localhost:8000/menus/2 - меню с id 2

http://localhost:8000/menus/{num}/submenus - список подменю

http://localhost:8000/menus/2/submenus/3 - подменю с id 3 в меню 2

http://localhost:8000/menus/{num}/submenus/{num}/dishes/ - список блюд

http://localhost:8000/menus/2/submenus/3/dishes/4 - блюдо 4, подменю 3, меню 2

## Launch
```shell
uvicorn main:app --reload
```
