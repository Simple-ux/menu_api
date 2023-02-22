from fastapi import FastAPI, Response
from database import *




app = FastAPI()

# CRUD MENU

# кол-во субменю в одном меню
async def submenus_count():
    menu_response = session.query(Menu).all()

    for item in menu_response:
        item.submenu_count = session.query(SubMenu).filter(SubMenu.menu_id == item.id).count()

        session.query(Menu).filter(Menu.id == item.id).update(
            {"submenu_count":item.submenu_count,
            "dishes_count": await dishes_count_menu(item.id)},
            synchronize_session = False)
        
    session.commit()


# Все меню
@app.get('/api/v1/menus')
async def get_all_menu():

    await submenus_count()
    menu_response = session.query(Menu).all()
    return menu_response



# Одно меню
@app.get('/api/v1/menus/{api_menu_id}')
async def get_one_menu(api_menu_id, response: Response):
    
    menu_response = {}
    if api_menu_id != 'null':
        menu_response = session.query(Menu).filter(Menu.id == api_menu_id).all()
        return menu_response
    else:
        menu_response["id"] = None
        menu_response["title"] = None
        menu_response["description"] = None
        return menu_response


# Создать меню
@app.post('/api/v1/menus', status_code=201)
async def create_menu():

    new_menu = Menu(title = "new", desc = "menu")
    session.add(new_menu)
    session.commit()
    
    return "Complite!"


# Обновить меню
@app.patch('/api/v1/menus/{api_menu_id}')
async def patch_menu(api_menu_id: int, response: Response):

    menu_response = session.query(Menu).filter(Menu.id == api_menu_id).update({"title":"patched title"}, synchronize_session = False)
    
    if menu_response == 1:
        session.commit()
    else:
        response.status_code = 404
        return response

    return "Complete"


# Удалить меню
@app.delete('/api/v1/menus/{api_menu_id}')
async def delete_menu(api_menu_id: int):

    menu_response = session.query(Menu).filter(Menu.id == api_menu_id).one()
    session.delete(menu_response)
    session.commit()
    return "Deleted"







# CRUD SUBMENU

# кол-во блюд в одном подменю
async def dishes_count_submenu():
    submenu_response = session.query(SubMenu).all()

    for item in submenu_response:
        item.dishes_count = session.query(Dishes).filter(Dishes.submenu_id == item.id).count()
        session.query(SubMenu).filter(SubMenu.id == item.id).update({'dishes_count': item.dishes_count})

    session.commit()
    return submenu_response


# кол-во блюд в одном меню
async def dishes_count_menu(api_menu_id):

    submenu_response = session.query(SubMenu).filter(SubMenu.menu_id == api_menu_id).all()
    sum = 0
    for item in submenu_response:
        sum += int(session.query(Dishes).filter(Dishes.submenu_id == item.id).count())
    return sum


# Все подменю
@app.get('/api/v1/menus/{api_menu_id}/submenus')
async def get_all_submenu(api_menu_id:int):

    await dishes_count_submenu()

    submenu_response = session.query(SubMenu).filter(SubMenu.menu_id == api_menu_id).all()
    return submenu_response


# Одно подменю
@app.get('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}')
async def get_all_submenu(api_menu_id:int, api_submenu_id:int):

    submenu_response = session.query(SubMenu).filter(SubMenu.id == api_submenu_id, SubMenu.menu_id == api_menu_id).one()
    return submenu_response


# Создать подменю
@app.post('/api/v1/menus/{api_menu_id}/submenus')
async def create_submenu(api_menu_id:int):

    new_submenu = SubMenu(title = "new", desc = "menu", menu_id = api_menu_id)
    session.add(new_submenu)
    session.commit()
    return "Complite!"


# Обновить подменю
@app.patch('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}')
async def patch_submenu(api_menu_id: int, api_submenu_id:int, response: Response):

    submenu_response = session.query(SubMenu).filter(SubMenu.id == api_submenu_id).update({"title":"patched submenu"}, synchronize_session = False)
    
    if submenu_response == 1:
        session.commit()
    else:
        response.status_code = 404
        return response

    return "Complete"


# Удалить подменю
@app.delete('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}')
async def delete_submenu(api_submenu_id: int, response: Response):

    submenu_response = session.query(SubMenu).filter(SubMenu.id == api_submenu_id).one()
    session.delete(submenu_response)
    session.commit()
    return "Deleted"



# CRUD DISHES

# Все блюда
@app.get('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}/dishes')
async def get_all_dishes(api_submenu_id:int):

    dishes_response = session.query(Dishes).filter(Dishes.submenu_id == api_submenu_id).all()
    return dishes_response


# Одно блюдо
@app.get('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}/dishes/{api_dish_id}')
async def get_one_dish(api_menu_id:int, api_submenu_id:int, api_dish_id:int, response: Response):

    try:
        submenu_response = session.query(Dishes).filter(
            Dishes.id == api_dish_id,
            Dishes.submenu_id == api_submenu_id,
            SubMenu.menu_id == api_menu_id).one()
    
    except:
        response.status_code = 404
        return response

    return submenu_response


# Создать блюдо
@app.post('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}/dishes')
async def create_dish(api_menu_id:int, api_submenu_id:int):

    new_dish = Dishes(title = "new", desc = "dish", price = "66.66", submenu_id = api_submenu_id)
    session.add(new_dish)
    session.commit()
    return "Complite!"


# Обновить блюдо
@app.patch('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}/dishes/{api_dish_id}')
async def patch_dish(api_menu_id: int, api_submenu_id:int, api_dish_id:int, response: Response):

    dish_response = session.query(Dishes).filter(Dishes.id == api_dish_id, Dishes.submenu_id == api_submenu_id).update(
        {"title":"patched dish"}, synchronize_session = False)

    if dish_response == 1:
        session.commit()
    else:
        response.status_code = 404
        return response

    return "Complete"


# Удалить блюдо
@app.delete('/api/v1/menus/{api_menu_id}/submenus/{api_submenu_id}/dishes/{api_dish_id}')
async def delete_dish(api_submenu_id: int, api_dish_id:int, response: Response):

    dish_response = session.query(Dishes).filter(Dishes.id == api_dish_id, Dishes.submenu_id == api_submenu_id).one()
    session.delete(dish_response)
    session.commit()
    return "Deleted"