import os

class TemplateEngine():

    def __init__(self) -> None:
        self.meta = {""}
        self.css = []
        self.title = 'FRAMEWORK TUTORIAL'
        self.base_path = os.path.join(os.getcwd(),'static')

    def render(self):
        pass



    def base_template(self,body:str):
        return f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="/static/favicon.ico">
        <title>BekoWork Framework</title>
    </head>
    <body>
        {body}
    </body>
</html>
        """

        # {% %}
        # {{}}