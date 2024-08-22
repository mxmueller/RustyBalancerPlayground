from flask import Flask, request, render_template_string
import numpy as np
import time
import psutil

app = Flask(__name__)

# HTML-Template für das Frontend
HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RustyBalancer Playground</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; text-align: center; }
        button { padding: 10px 20px; margin: 10px; font-size: 16px; cursor: pointer; }
        #status { margin-top: 20px; padding: 10px; background-color: #f0f0f0; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>RustyBalancer Playground</h1>
    <div>
        <button onclick="runOperation('/cpu?duration=5')">CPU Load (5s)</button>
        <button onclick="runOperation('/cpu?duration=10')">CPU Load (10s)</button>
        <button onclick="runOperation('/memory?size=100')">Memory Load (100MB)</button>
        <button onclick="runOperation('/memory?size=500')">Memory Load (500MB)</button>
        <button onclick="runOperation('/combined?cpu_duration=5&mem_size=100')">Combined Load</button>
    </div>
    <div id="status">Status: Idle</div>

    <script>
        function runOperation(endpoint) {
            document.getElementById('status').innerHTML = 'Status: Running operation...';
            fetch(endpoint)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('status').innerHTML = 'Status: ' + data;
                    updateResourceUsage();
                });
        }

        function updateResourceUsage() {
            fetch('/status')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('status').innerHTML += '<br>' + data;
                });
        }

        // Update resource usage every 5 seconds
        setInterval(updateResourceUsage, 5000);
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/cpu')
def cpu_intensive():
    duration = int(request.args.get('duration', 5))
    start_time = time.time()
    while time.time() - start_time < duration:
        np.linalg.inv(np.random.rand(500, 500))
    return f"CPU-intensive operation completed in {duration} seconds."

@app.route('/memory')
def memory_intensive():
    size = int(request.args.get('size', 100))  # Size in MB
    data = ' ' * (size * 1024 * 1024)  # Allocate memory
    time.sleep(2)  # Hold the memory for 2 seconds
    del data  # Release the memory
    return f"Memory-intensive operation completed. Allocated {size} MB."

@app.route('/combined')
def combined():
    cpu_duration = int(request.args.get('cpu_duration', 5))
    mem_size = int(request.args.get('mem_size', 100))
    
    # CPU-intensive operation
    start_time = time.time()
    while time.time() - start_time < cpu_duration:
        np.linalg.inv(np.random.rand(500, 500))
    
    # Memory-intensive operation
    data = ' ' * (mem_size * 1024 * 1024)
    time.sleep(2)
    del data
    
    return f"Combined operation completed. CPU duration: {cpu_duration}s, Memory allocated: {mem_size} MB."

@app.route('/status')
def status():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    return f"Current CPU usage: {cpu_percent}%, Memory usage: {memory_percent}%"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)