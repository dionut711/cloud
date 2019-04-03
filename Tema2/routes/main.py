home_page_path = "pages/home.html"

def home_page(server):
    server.send_response(200)
    server.send_header('Content-type','text/html')
    server.end_headers()
    with open(home_page_path, "rb") as fd:
        server.wfile.write(fd.read())

def styles(server):
    server.send_response(200)
    server.send_header('Content-type','text/html')
    server.end_headers()
    with open("." + server.path, "rb") as fd:
        server.wfile.write(fd.read())
        