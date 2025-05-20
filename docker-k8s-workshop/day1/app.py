from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Setup basic logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info("Root endpoint called.")
    return jsonify(message="Hello, World from Flask in Docker!")

@app.route('/health')
def health_check():
    app.logger.info("Health check endpoint called.")
    return jsonify(status="UP"), 200

if __name__ == '__main__':
    app.logger.info("Starting Flask app on port 8080...")
    app.run(host='0.0.0.0', port=8080)
