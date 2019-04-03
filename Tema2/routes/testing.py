def get(server):
    server.send_response(200)
    server.send_header('Content-type','text/html')
    server.end_headers()
    server.wfile.write("<div> GET request test </div>".encode())

def post(server):
    server.send_response(200)
    server.send_header('Content-type','text/html')
    server.end_headers()
    server.wfile.write("<div> POST request test </div>".encode())

def delete(server):
    server.send_response(200)
    server.send_header('Content-type','text/html')
    server.end_headers()
    server.wfile.write("<div> DELETE request test </div>".encode())

def put(server):
    server.send_response(200)
    server.send_header('Content-type','text/html')
    server.end_headers()
    server.wfile.write("<div> PUT request test </div>".encode())