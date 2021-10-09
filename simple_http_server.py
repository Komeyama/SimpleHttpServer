import http.server

handler = http.server.SimpleHTTPRequestHandler

with http.server.HTTPServer(("localhost", 8080), handler) as server:
	print("start server at ", server.server_address)
	server.serve_forever()