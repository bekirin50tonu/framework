from pyclbr import Function
from typing import Callable
import re

from core.router.manager import RouteManager

class Route:

    __manager = RouteManager()
    
    __prefix = ['']

    __patterns = {
        "int": r'([0-9]*)',
        "str":r'([a-zA-Z0-9]*)'
    }

    @staticmethod
    def __register_route(action,method:str,path,name):
        register_path = f"{'/'.join(x for x in Route.__prefix)}{path}"
        preg_path = register_path
        match= re.findall(r'(\<(.*?)\:(.*?)\>)',register_path)
        for x in match:
            preg_path= register_path.replace(x[0],Route.__patterns.get(x[2]))
        preg_path = f"^{preg_path}$"
        print(register_path)
        # print(match)
        route_pattern = {
            "name":name or path,
            "callback": action,
            "path":register_path,
            "preg":preg_path
        }
        Route.__manager.add(method,route_pattern)   

    @staticmethod
    def get(path:str,action:Function,name:str):
        Route.__register_route(action,'GET',path,name)
        # print(Route.__prefix)
        return Route

    @staticmethod
    def prefix(prefix:str):
        def call(func:Callable):
            Route.__prefix.append(prefix)
            func()
            Route.__prefix.remove(prefix)
            return None
        return call
    
    @staticmethod
    def get_routes() -> dict:
        return Route.__manager.all()

    def has_route(method:str,path:str)->bool:
        return Route.__manager.has(method,path)

    def match_route(method:str,path:str):
        return Route.__manager.match(method,path)
    
    def get_route(method:str,path:str):
        return Route.__manager.get(method,path)
