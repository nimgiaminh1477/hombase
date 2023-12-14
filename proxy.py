from http.server import SimpleHTTPRequestHandler, HTTPServer
from http.client import HTTPConnection
from urllib.parse import urlparse
import json

class ProxyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.proxy_request()

    def do_POST(self):
        self.proxy_request()

    def proxy_request(self):
        # Parse the original request URL
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parsed_url.query

        # Set up connection to Express API
        express_api_host = 'localhost'
        express_api_port = 3000
        express_api_path = path + ('?' + query if query else '')
        express_api_connection = HTTPConnection(express_api_host, express_api_port)

        try:
            # Read the request body from the client
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)

            # Forward the request to Express API
            express_api_connection.request(self.command, express_api_path, body, self.headers)
            express_response = express_api_connection.getresponse()

            # Send the Express API response back to the client
            self.send_response(express_response.status)
            for header, value in express_response.getheaders():
                self.send_header(header, value)
            self.end_headers()
            self.wfile.write(express_response.read())

        except Exception as e:
            print(f"Error forwarding request: {e}")

        finally:
            express_api_connection.close()

if __name__ == "__main__":
    proxy_port = 8001
    proxy_server_address = ('', proxy_port)

    with HTTPServer(proxy_server_address, ProxyHandler) as proxy_server:
        print(f"Proxy server is running on http://localhost:{proxy_port}")
        proxy_server.serve_forever()