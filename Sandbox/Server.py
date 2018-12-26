from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from sandbox import Sandbox

class PostHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        self._set_response()
        raw_str = self.rfile.read(length)
        json_body = json.loads(raw_str)
        print(json_body)

def ConstructHandler(sandbox):
    class PostHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            self.sandbox = sandbox
            #self.sandbox.load_map('demo.graphml', '../Viz/data/')
            super(PostHandler, self).__init__(*args, **kwargs)

        def _set_response(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()

        def do_POST(self):
            length = int(self.headers['Content-Length'])
            self._set_response()
            raw_str = self.rfile.read(length)
            json_body = json.loads(raw_str)

            print(json_body)
            try:
                req_type = json_body['type']
                if req_type == 'new':
                    plan = self.sandbox.add_vehicle(json_body)
                    self.wfile.write(json.dumps(plan).encode('utf-8'))
                elif req_type == 'pos':
                    self.sandbox.update_vehicle(json_body)
            except:
                pass

    
    return PostHandler


def start_server(address=('127.0.0.1', 8888), post_handler=PostHandler):
    httpd = HTTPServer(address, post_handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
        

if __name__ == '__main__':
    start_server()
    
    
