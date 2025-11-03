import os
import socket
from flask import Flask

# 1. Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def main_dashboard():
    # 2. Collect dynamic information
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
    except:
        host_name = "Hostname Unavailable"
        host_ip = "IP Unavailable"

    # 3. Read an environment variable (set in docker-compose)
    app_message = os.environ.get('CUSTOM_MESSAGE', 'A generic message from the default environment.')
    
    # 4. Create the interesting output (using basic HTML for visual structure)
    html_output = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Container Environment Dashboard</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #282c34; color: #61dafb; text-align: center; padding: 50px; }}
            h1 {{ color: #ffffff; border-bottom: 2px solid #61dafb; padding-bottom: 10px; }}
            .info-box {{ margin: 20px auto; padding: 15px; border: 1px solid #61dafb; border-radius: 8px; width: 80%; max-width: 600px; background-color: #1f232a; }}
            p {{ font-size: 1.1em; text-align: left; margin: 5px 0; }}
            strong {{ color: #a900ff; }}
        </style>
    </head>
    <body>
        <h1>🚀 Docker Flask App - Environment Dashboard</h1>
        <div class="info-box">
            <p><strong>App Status:</strong> Running inside Docker Container</p>
            <p><strong>Container Hostname:</strong> {host_name}</p>
            <p><strong>Container IP:</strong> {host_ip}</p>
        </div>
        
        <div class="info-box" style="border-color: #ff9800;">
            <p><strong>Custom Environment Message:</strong></p>
            <p style="font-size: 1.2em; color: #ff9800;">"{app_message}"</p>
        </div>

    </body>
    </html>
    """
    return html_output

if __name__ == "__main__":
    # Note: When running with Docker/Gunicorn/Waitress, the app.run() block often isn't used.
    # We include it here for local development sanity.
    app.run(host='0.0.0.0', port=5000)