from fileinput import filename
import os
from pathlib import Path 


class Response:
    def __init__(self,template,content,type:str="text/html") -> None:
        self.template = template
        self.content = content
        self.type = type


class HTTPResponse(Response):

    def __init__(self, template:Path, content, type: str = "text/html"):
        super().__init__(template, content, type)
        self.base_path = os.getcwd()
        file_name = os.path.join(self.base_path,template)
        self.template_text = open(file_name,'r',encoding='utf-8').read().format(**content).encode('utf-8')

    def execute(self):
        return (self.template_text,self.type)

    def redirect():
        pass

    def to():
        pass


class JSONResponse:
    def __init__(self) -> None:
        pass

class ImageResponse:
    def __init__(self,path) -> None:
        self.base_path = os.path.join(os.getcwd(),path)
        self.type = 'image/*'


    def execute(self):
        image = open(self.base_path,'rb').read()
        return (image,self.type)

