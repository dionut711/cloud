import logs

def do_GET(handler):
        handler.send_response(200)
        handler.send_header('Content-type','text/html')
        handler.end_headers()

        html = str(logs.get_all_json())
        handler.wfile.write(html.encode())