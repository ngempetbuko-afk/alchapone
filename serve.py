import http.server
import socketserver
import sys

DEV_PORT = 47315
DIRECTORY = r"C:\Users\hans_\AppData\Local\Temp\opencode\repo-inspect-23bfe77a\alchapone"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    print(f"Starting alchapone dev server on http://127.0.0.1:{DEV_PORT}/")
    try:
        with socketserver.TCPServer(("127.0.0.1", DEV_PORT), Handler) as httpd:
            httpd.serve_forever()
    except OSError as e:
        print(f"Error binding to port {DEV_PORT}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run()
