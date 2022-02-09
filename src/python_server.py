from http.server import HTTPServer, SimpleHTTPRequestHandler
from transformers import pipeline

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ("0.0.0.0", 8000)
    httpd = server_class(server_address, handler_class)
    print("launching server...")

    classifier = pipeline("sentiment-analysis")
    result = classifier("It is easy to test one statement inside a server inference request")
    print(result[0]['label'])
    httpd.serve_forever()

if __name__ == "__main__":
    run()

