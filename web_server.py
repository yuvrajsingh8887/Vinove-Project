from flask import Flask, render_template, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    screenshots = os.listdir('screenshots')
    screenshots_data = []
    
    for filename in screenshots:
        if filename == 'metadata.json':  # Skip the metadata.json file
            continue
        
        file_path = os.path.join('screenshots', filename)
        file_time = os.path.getmtime(file_path)
        formatted_time = datetime.fromtimestamp(file_time).strftime('%Y-%m-%d %H:%M:%S')
        screenshots_data.append({'filename': filename, 'timestamp': formatted_time})

    return render_template('index.html', screenshots=screenshots_data)

@app.route('/screenshots/<filename>')
def get_screenshot(filename):
    return send_from_directory('screenshots', filename)

def start_server():
    app.run(debug=True, port=5000, use_reloader=False)

if __name__ == "__main__":
    start_server()
