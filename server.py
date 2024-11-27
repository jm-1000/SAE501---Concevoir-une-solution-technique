import http.server
import socketserver
import json

PORT = 8080

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        response_data = {
            "utilisateurs": [
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "1",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "2",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                },
                {
                    "id": "3",
                    "nom": "John Doe",
                    "mail": "johndoe@example.com",
                    "passwd": "zdqe3zSZ3Z",
                    "status": "active"
                },
                {
                    "id": "4",
                    "nom": "Dian Sue",
                    "mail": "diansue@example.com",
                    "passwd": "ADEaezadeZ3Z",
                    "status": "active"
                }
            ]
        }
        response_json = json.dumps(response_data)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_json)))
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:3000') 
        self.send_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
        self.end_headers()
        self.wfile.write(response_json.encode('utf-8'))
    

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        print(json.loads(post_data))
        response_data = { "received": "yes" } 
        response_json = json.dumps(response_data) 
        self.send_response(201) 
        self.send_header('Content-Type', 'application/json') 
        self.send_header('Content-Length', str(len(response_json))) 
        self.end_headers() 
        self.wfile.write(response_json.encode('utf-8'))


Handler = SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
