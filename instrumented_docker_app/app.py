from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    result = 100 / int(logger.name)  # This will raise ZeroDivisionError
    return f"Result: {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)