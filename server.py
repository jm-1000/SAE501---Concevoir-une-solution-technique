import http.server
import socketserver
import json

import sqlite3


def create():
    try:
        c.execute("""CREATE TABLE utilisateurs (login, email)""")
    except:
        pass


def insert(nom, email):
    c.execute("INSERT INTO utilisateurs (login, email) VALUES (?, ?)", (nom, email))
    conn.commit()


path= r'C:\Users\tmegh\Desktop\SAE501-TP\database.db'
conn = sqlite3.connect(path)
c= conn.cursor()
conn.commit()


PORT = 8080

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        c.execute("SELECT rowid, login, email FROM utilisateurs")
        utilisateurs = c.fetchall()

        response_data = {
            "utilisateurs": [
                {
                    "id": str(row[0]),
                    "nom": row[1],
                    "mail": row[2],
                    "passwd": "motdepasse_placeholder",  
                    "status": "active"
                } for row in utilisateurs
            ]
        }
        
        response_json = json.dumps(response_data)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_json)))
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
        self.end_headers()
        self.wfile.write(response_json.encode('utf-8'))
       
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        data = json.loads(post_data)

        insert(data['nom'], data['mail'])

        response_data = {"received": "yes"} 
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
c.close()