from flask import Flask, jsonify, render_template_string
import subprocess
import os

app = Flask(__name__)

# Store the process globally
process = None

@app.route('/')
def simple_page():
    # Inline HTML content as a simple page without a template
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python App Launcher</title>
        <script>
            function launchApp() {
                fetch('/launch', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => alert(data.status))
                    .catch(error => console.error('Error launching app:', error));
            }

            function closeApp() {
                fetch('/close', { method: 'POST' })
                    .then(response => response.json())
                    .then(data => alert(data.status))
                    .catch(error => console.error('Error closing app:', error));
            }
        </script>
    </head>
    <body>
        <h1>Launch Exploid</h1>
        <button onclick="launchApp()">Use Exploid</button>
        <button onclick="closeApp()">Close Exploid</button>
    </body>
    </html>
    '''
    return render_template_string(html_content)

@app.route('/launch', methods=['POST'])
def launch():
    global process
    exe_path = r'C:\xampp\htdocs\Exploid\Exploid\Exploid.exe'  # Corrected file path

    # Start the .exe file if not already running
    if not process:
        process = subprocess.Popen(exe_path)
        return jsonify({'status': 'Python app launched'})
    else:
        return jsonify({'status': 'App is already running'})

@app.route('/close', methods=['POST'])
def close():
    global process
    if process:
        # Terminate the Python executable process
        process.terminate()
        process = None
        return jsonify({'status': 'Python app closed'})
    else:
        return jsonify({'status': 'No app running'})

if __name__ == '__main__':
    app.run(debug=True)
