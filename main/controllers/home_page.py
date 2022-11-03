

from core.response import HTTPResponse,ImageResponse


def index(request,id):
        content = {
                "title":"Bu bir denemedir",
                "message":"bu deneme mesajıdır",
                "path":request.path,
                "number":id,
                "numbers":list(range(100))
        }
        return HTTPResponse('static\index.html',content)

def icon(request,path):
        return ImageResponse(r'static\favicon.ico')