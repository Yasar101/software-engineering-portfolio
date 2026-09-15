"""Minimal local HTTP transport for the framework-neutral item service."""

from __future__ import annotations

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json

from .api import ItemService, MemoryItemRepository


def make_handler(service: ItemService) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def _send(self, status: int, body: dict[str, object]) -> None:
            encoded = json.dumps(body).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/health":
                self._send(200, {"status": "ok", "storage": "in-memory demo adapter"})
            elif self.path == "/items":
                status, body = service.list(); self._send(status, body)
            elif self.path.startswith("/items/") and self.path[7:].isdigit():
                status, body = service.retrieve(int(self.path[7:])); self._send(status, body)
            else:
                self._send(404, {"error": "route not found"})

        def do_POST(self) -> None:  # noqa: N802
            if self.path != "/items":
                self._send(404, {"error": "route not found"}); return
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if length > 16_384:
                    raise ValueError("request body too large")
                payload = json.loads(self.rfile.read(length))
                if not isinstance(payload, dict):
                    raise ValueError("JSON object required")
            except (ValueError, json.JSONDecodeError):
                self._send(400, {"error": "invalid JSON request body"}); return
            status, body = service.create(payload); self._send(status, body)

        def log_message(self, *_: object) -> None:
            return
    return Handler


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Run the local portfolio API demo.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8001, type=int)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), make_handler(ItemService(MemoryItemRepository())))
    print(f"Local demo API listening at http://{args.host}:{args.port} (in-memory adapter; not PostgreSQL).")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
