import configparser
import json

from flask import Flask
from flask import jsonify

config = configparser.ConfigParser()

# try to load the config file
try:
    config.read("config.ini")
    path = config["SERVER"]["Input"]
except (IOError, KeyError):
    print("config.ini not found")
    pass


app = Flask(__name__)


@app.route('/')
def profiler_json():
    with app.app_context():
        with open(path, encoding="utf8") as f:
            data = json.loads(f.read())
            return jsonify(data)


if __name__ == '__main__':
    app.run()
