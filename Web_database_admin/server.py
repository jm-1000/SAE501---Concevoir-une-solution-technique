#!/usr/bin/python3.11

import json
import string
import random  
import http.server
import socketserver
import mysql.connector # sudo apt-get install python3-mysql.connector
 

FRONTEND = "/Frontend/index.html"
PORT = 8000
DB_USERNAME = "adm-radius"
DB_PASSWORD = "r2d??sp2s"
DB_HOST = "192.168.40.6"
DB_NAME = "radius"

class HttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self): 
        if self.path == "/":
            self.path = FRONTEND
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        if self.path == "/users":
            self.get_users()


    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length) 
        data = json.loads(post_data) 
        if 'id' in data:
            request_sql('delete', (data['id'],))
        if 'name' in data:
            request_sql('insert', (
                                    data['name'], 
                                    data['mail'], 
                                    generate_password())
            )
        self.send_response(201)
        self.end_headers()
        

    def get_users(self): 
        users = request_sql("users")
        login = {item[0]: item[1] for item in request_sql('login')}
        get_login = lambda u: str(login[u])[:16] if u in login.keys() else "jamais"
        self.send_response(200)
        if users:
            response = {
                "users": [
                    {
                        "id": str(user[0]),
                        "name": user[1],
                        "passwd": user[2],  
                        "mail": user[3],
                        "login": get_login(user[1])
                    } for user in users
                ]
            }
            response_json = json.dumps(response)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(response_json)))
            self.end_headers()
            self.wfile.write(response_json.encode('utf-8'))
        else: self.end_headers()


def request_sql(type:str, params=None):
    db = mysql.connector.connect(
                    user=DB_USERNAME, 
                    password=DB_PASSWORD, 
                    host=DB_HOST, 
                    database=DB_NAME
        ) 
    CURSOR_DB = db.cursor() 
    if params:
        if type == 'delete':
            CURSOR_DB.execute(
                "DELETE FROM radpostauth " +
                "WHERE username = " +
                "(SELECT username FROM radcheck WHERE id=%s)", 
                params
            )
            CURSOR_DB.execute(
                "DELETE FROM radcheck WHERE id=%s", 
                params
            )
        elif type == 'insert':
            CURSOR_DB.execute(
                "INSERT INTO radcheck " +
                "(username, email, value) " +
                "VALUES (%s, %s, %s)", 
                params
            )
        db.commit()
        CURSOR_DB.close()
    else:
        if type == 'users':
            CURSOR_DB.execute(
                "SELECT id, username, value, email FROM radcheck"
            )
        elif type == 'login':
            CURSOR_DB.execute(
                "SELECT username, MAX(authdate) AS last_login FROM radpostauth " +
                "WHERE reply = 'Access-Accept' GROUP BY username"
            )
        data = CURSOR_DB.fetchall()
        CURSOR_DB.close()
        return data
    
     
def generate_password(length=10):  
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))  


with socketserver.TCPServer(("", PORT), HttpHandler) as httpd:
    print("Port utilisé :", PORT)
    httpd.serve_forever()
