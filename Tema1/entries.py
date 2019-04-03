import services

def do_GET(handler):
    handler.send_response(200)
    handler.send_header('Content-type','text/html')
    handler.end_headers()
    html = ""
    for i, entry in enumerate(services.apis_service.GetAllEntries()):
        html += "<option value={}> {} </option>\n".format(entry.link, entry.name)
    handler.wfile.write(html.encode())
