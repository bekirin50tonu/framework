


from core.router import Route
import main.controllers.home_page as main

Route.get('/',main.index,'index')

Route.get('/static/favicon.ico',main.icon,'icon')

@Route.prefix('users')
def _users():
    Route.get('',main.index,'user_index')

    @Route.prefix('get')
    def _gets():
        Route.get('',main.index,'get_users')
        Route.get('/<id:int>',main.index,'get_users')

@Route.prefix('post')
def _post():
    Route.get('',main.index,'indsex')