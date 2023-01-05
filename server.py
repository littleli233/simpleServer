from flask import Flask, Response
from markupsafe import escape
import argparse

server = Flask(__name__)

@server.route("/")
def index():
    try:
        with open("index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return Response(None, status=404)

@server.route("/<path:path>")
def load(path):
    try:
        with open(escape(path), "r") as f:
            return f.read()
    except FileNotFoundError:
        return Response(None, status=404)

def cli():
    parser = argparse.ArgumentParser(description="SimpleServer")
    parser.add_argument("-host", help="host", required=True)
    parser.add_argument("-port", help="port", required=True)
    parser.add_argument("-pubkey", help="ssl certificate")
    parser.add_argument("-prikey", help="ssl private key")
    args = parser.parse_args()
    if hasattr(args, "-h"):
        parser.print_help()
    if not (args.pubkey == None and args.prikey == None):
        server.run(host=args.host, port=args.port, ssl_context=(args.pubkey, args.prikey))
    else:
        server.run(host=args.host, port=args.port)

if __name__ == "__main__":
    cli()
