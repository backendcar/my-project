from http.server import HTTPServer,BaseHTTPRequestHandler

HOST = "192.168.1.104"
PORT = 9999

class TestHttp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1 style='color:purple;'>Roxo</h1></body></html>","utf-8"))


server = HTTPServer((HOST,PORT),TestHttp)
print("Server is running ...")

server.serve_forever()
server.server_close()
print("server stop ...")
