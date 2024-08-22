Sure! Here’s a basic `README.md` template for your repository that you can customize further as needed:

---

# RustyBalancer Playground

RustyBalancer Playground is a simple web application built with Flask that simulates CPU and memory-intensive operations. This application allows users to generate load on the server and observe resource usage in real-time.

## Features

- **CPU Load Simulation:** Generate CPU load for a specified duration.
- **Memory Load Simulation:** Allocate and hold a specified amount of memory for a brief period.
- **Combined Load:** Perform both CPU and memory-intensive operations simultaneously.
- **Real-time Resource Monitoring:** View the current CPU and memory usage of the server.

## Prerequisites

- Docker
- Python 3.9+ (for local testing)

## Setup and Installation

### Docker

1. **Build the Docker image:**

   ```bash
   docker build -t rustybalancer-playground:local .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -d -p 5000:5000 --name rustybalancer-playground-local rustybalancer-playground:local
   ```

3. **Access the application:**

   Open your web browser and navigate to `http://localhost:5000`.

### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/rustybalancer-playground.git
   cd rustybalancer-playground
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

4. **Access the application:**

   Open your web browser and navigate to `http://localhost:5000`.

## Usage

### CPU Load

- **5-second CPU load:** Click the "CPU Load (5s)" button.
- **10-second CPU load:** Click the "CPU Load (10s)" button.

### Memory Load

- **100MB memory allocation:** Click the "Memory Load (100MB)" button.
- **500MB memory allocation:** Click the "Memory Load