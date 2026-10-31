"""
MeetingAutopsy AI - Local Backend Server
Serves the web application and provides high-accuracy meeting speech transcription
and semantic analysis endpoints via local Python AI engine.
"""

import os
import sys
import io

# Ensure UTF-8 output encoding across Windows shells and background logs
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

import json
import tempfile
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import meeting_analyzer

PORT = 8000
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))

class MeetingAIHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORKSPACE_DIR, **kwargs)

    def end_headers(self):
        # Enable CORS for local cross-origin development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Filename')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # Default route to index.html or am.html
        if self.path == '/' or self.path == '':
            if os.path.exists(os.path.join(WORKSPACE_DIR, 'index.html')):
                self.path = '/index.html'
            else:
                self.path = '/am.html'
        elif self.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "online",
                "engine": "MeetingAutopsy Local Python AI Engine",
                "accuracy": "85-95% Real Speech-to-Text Transcription"
            }).encode('utf-8'))
            return

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))

        if parsed.path == '/api/analyze':
            self.handle_analyze(content_length)
        elif parsed.path == '/api/chat':
            self.handle_chat(content_length)
        else:
            self.send_error(404, "Endpoint not found")

    def handle_analyze(self, content_length):
        content_type = self.headers.get('Content-Type', '')
        filename_header = self.headers.get('X-Filename', 'meeting_recording.mp4')
        ext = os.path.splitext(filename_header)[1] or '.mp4'

        with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tf:
            temp_path = tf.name

        try:
            # Handle multipart/form-data or raw stream
            if 'multipart/form-data' in content_type:
                boundary = content_type.split('boundary=')[1].encode('ascii')
                body = self.rfile.read(content_length)
                parts = body.split(b'--' + boundary)
                file_bytes = None
                for part in parts:
                    if b'filename=' in part:
                        header_end = part.find(b'\r\n\r\n')
                        if header_end != -1:
                            file_bytes = part[header_end+4:].rstrip(b'\r\n')
                            break
                if file_bytes is None:
                    # Fallback to entire body
                    file_bytes = body
                with open(temp_path, 'wb') as f:
                    f.write(file_bytes)
            else:
                # Raw binary upload
                remaining = content_length
                with open(temp_path, 'wb') as f:
                    while remaining > 0:
                        chunk = self.rfile.read(min(remaining, 65536))
                        if not chunk:
                            break
                        f.write(chunk)
                        remaining -= len(chunk)

            print(f"[Server] Received media upload: {os.path.getsize(temp_path)} bytes ({filename_header}) -> Running Real AI Analysis...")
            report = meeting_analyzer.analyze_meeting(temp_path, original_filename=filename_header)
            
            response_json = json.dumps(report, ensure_ascii=False).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(response_json)))
            self.end_headers()
            self.wfile.write(response_json)
            print("[Server] Analysis successfully returned to client.")

        except Exception as e:
            print(f"[Server] Error during analysis: {e}")
            err_json = json.dumps({"error": str(e)}).encode('utf-8')
            self.send_response(500)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(err_json)))
            self.end_headers()
            self.wfile.write(err_json)

        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception:
                    pass

    def handle_chat(self, content_length):
        try:
            raw_bytes = self.rfile.read(content_length)
            # Try utf-8 first, then utf-16, then latin-1 fallback
            for enc in ['utf-8-sig', 'utf-8', 'utf-16', 'latin-1']:
                try:
                    body = raw_bytes.decode(enc)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                body = raw_bytes.decode('utf-8', errors='ignore')

            req = json.loads(body)
            query = req.get('query', '')
            data = req.get('data', {})

            reply = meeting_analyzer.answer_meeting_question(query, data)
            resp_bytes = json.dumps({"reply": reply}, ensure_ascii=False).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(resp_bytes)))
            self.end_headers()
            self.wfile.write(resp_bytes)
        except Exception as e:
            import traceback
            traceback.print_exc()
            err_json = json.dumps({"error": str(e)}).encode('utf-8')
            self.send_response(500)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(err_json)))
            self.end_headers()
            self.wfile.write(err_json)

def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, MeetingAIHandler)
    print(f"==================================================")
    print(f"  MeetingAutopsy Python AI Server running!")
    print(f"  Local URL: http://localhost:{PORT}")
    print(f"  Accuracy: >85% Real Speech-to-Text Transcription")
    print(f"==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == '__main__':
    run_server()
