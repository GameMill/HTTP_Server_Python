from http.server import BaseHTTPRequestHandler, HTTPServer
import var_dump
import time
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
       
        try:

            Prams = self.Get_Prams()
            Url = self.Get_Url()

            if(Url["Controller"] == "favicon.ico"):
                return
            module = __import__(Url["Controller"]+"_controller")
            class_ = getattr(module, Url["Controller"]+"_controller")
            instance = class_()
            method_to_call = getattr(instance, Url["Action"])

            method_to_call(self,Prams,Url)
            
            del instance
            del method_to_call
            del module
            del class_
        except:
            self.send_response(404)
            self.end_headers()
            pass
        

        # if(self.path == "/" or self.path.__contains__("/index.html") or self.path.__contains__("/?")):
        #     # var_dump.var_dump(self)
        #     self.send_response(200)
        #     self.send_header("Content-type", "text/html")
        #     self.end_headers()
        #     self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #     self.wfile.write(bytes(f"<p>Request: {self.path}</p>", "utf-8"))
        #     self.wfile.write(bytes("<body>", "utf-8"))
        #     self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #     self.wfile.write(bytes("</body></html>", "utf-8"))
    def Get_Prams(self):
        prams = {}
        data = self.path.split("?");
        if(data.__len__() == 2):
            Prams = data[1].split("&")
            for item in range(Prams.__len__()):
                info = Prams[item].split("=");
                if(info.__len__() == 1):
                    prams[info[0]] = ""
                else:
                    prams[info[0]] = info[1]
        return prams   


    def Get_Url(self):
        prams = {"Controller":"home","Action":"index","Full":[]}
        
        data = self.path.split("?")
        Urls = data[0].split("/")
        if(Urls.__len__() == 2 and Urls[1] == "index.html"):
            return prams
        
        if(Urls.__len__() == 2 and Urls[1] != ""):
            prams["Controller"] = Urls[1].lower()
        if(Urls.__len__() == 3 and Urls[2] != ""):
            prams["Action"] = Urls[2].lower()
        prams["Full"] = Urls
        return prams







if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


