"""
keep_alive.py - Web server to keep the bot alive on Railway.app
Railway keeps services alive as long as they bind to a PORT,
so this Flask server handles that requirement.
"""

import os
from flask import Flask
from threading import Thread
import logging

# Suppress Flask's default request logs to keep console clean
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def home():
    return "Zyrox Development™ 2025 — Bot is Online ✅"

@app.route('/health')
def health():
    return {"status": "ok"}, 200

def run():
    port = int(os.environ.get("PORT", 8080))  # Railway injects PORT automatically
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    """Start the web server in a background thread."""
    server = Thread(target=run, daemon=True)
    server.start()
    print(f"[keep_alive] Web server started on port {os.environ.get('PORT', 8080)}")
