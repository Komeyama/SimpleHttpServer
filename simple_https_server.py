import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("./server.pem")

handler = SimpleHTTPRequestHandler

with HTTPServer(("localhost", 8080), handler) as server:
    print("start https server at", server.server_address)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    server.serve_forever()