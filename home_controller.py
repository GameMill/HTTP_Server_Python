class home_controller:
    
    def index(self,bowser,Prams,Url):
        bowser.send_response(200)
        bowser.send_header("Content-type", "text/html")
        bowser.end_headers()
        bowser.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        bowser.wfile.write(bytes(f"<p>Request: {bowser.path}</p>", "utf-8"))
        bowser.wfile.write(bytes("<body>", "utf-8"))
        bowser.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        bowser.wfile.write(bytes("</body></html>", "utf-8"))
