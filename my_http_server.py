from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class MyHttpServer:

    def setup_server(self):
        httpd = HTTPServer(("localhost", 8080), self.MyHander)
        print("start server!")
        httpd.serve_forever()

    class MyHander(SimpleHTTPRequestHandler):

        def __init__(self, request, client_address, server):
                # define variable here.
                super().__init__(request, client_address, server)

        def do_GET(self):
            body = json.dumps({"request": "sucsess get!"})
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Content-length', len(body))
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))

        def do_POST(self):
            content_len = int(self.headers.get("content-length"))
            req_body = self.rfile.read(content_len).decode("utf-8")
            json_data = json.loads(req_body)
            print(json_data)

            response_message = {"request": "sucsess post!"}
            response_body = json.dumps(response_message)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response_body.encode("utf-8"))

my_http_server = MyHttpServer()
my_http_server.setup_server()         