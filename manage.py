import argparse
import sys
import re
import logging

from http.server import BaseHTTPRequestHandler, HTTPServer

from core.router import Route
import router.web


PACKAGE_NAME = 'BekoWork'
class WebServer(BaseHTTPRequestHandler):
    def set_header(self,type:str):
        self.send_response(200)
        self.send_header('Content-type',type)
        self.end_headers()
    def do_HEAD(self):
        self.set_header('text/html')

    def do_GET(self):
        path = self.path
        robot = ['/favicon.ico']
        print(self.path)
        if not path in robot:

            # If route is not in list
            match = Route.match_route('GET',path)
            if match[0] == None:
                self.set_header('text/html')
                return self.wfile.write(bytes(open('static\error.html','r',encoding='utf-8').read(),'utf-8'))
            data = match[0].callback(self,*match[1] or None).execute()
            self.set_header(data[1])
            return self.wfile.write(data[0])
    def do_POST(self):
        pass


class ManagerUtility:
    def __init__(self) -> None:
        self.__parser = self.__prepareArgument()

    def __prepareArgument(self) ->argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description=f'{PACKAGE_NAME} Framework \nHelp Commands')

        """Server Start Arguments"""
        starter = parser.add_argument_group(description='Start Server')
        starter.add_argument('-s','-start',required=True,help='This command is tried to start web server.', default='server',choices=['server'])
        starter.add_argument('-host',default='localhost',help='Start Host with `default: localhost`')
        starter.add_argument('-port',default=8080,type=int, help='Start Port with `default: 8080`')
        return parser
     
    def __prepareServer(self,options:dict):
        webServer = HTTPServer((options['host'], options['port']), WebServer)
        print("Server started http://%s:%s" % (options['host'], options['port']))

        try:
            webServer.serve_forever()
        except KeyboardInterrupt:
            pass

        webServer.server_close()
        print("Server stopped.")

    def execute(self):
        # args = sys.argv[1::]
        # if args[0] == 'run':
        #     self.__prepareServer(options=options)
        options = self.__parser.parse_args().__dict__
        if options['s'] == 'server' or options['start' == 'server']:
            self.__prepareServer(options=options)



if __name__ == '__main__':
    manager = ManagerUtility()
    manager.execute()
