

from ctypes import Union
from dataclasses import dataclass
from typing import Callable
import re

@dataclass
class RouteData:
    name:str
    path:str
    preg:str
    callback:Callable


class RouteManager:
    def __init__(self) -> None:
        self.gets = []
        self.post = []

    def add(self,method:str,options:dict) ->bool:
        try:
            data = RouteData(**options)
            if method.upper() == 'GET':
                self.gets.append(data)
            elif method.upper() == 'POST':
                self.post.append(data)
            else:
                raise Exception('Wrong Request Method')
        except:
            return False
        finally:
            return True
        
    def all(self):
        return {"GET":self.gets,'POST':self.post}

    def match(self,method:str,path:str):
        filtering_list = self.gets if method.upper() == 'GET' else self.post
        find:Union[None,RouteData] = next((x for x in filtering_list if len(re.findall(x.preg,path)) >0), None)
        return (find,re.findall(find.preg,path))

