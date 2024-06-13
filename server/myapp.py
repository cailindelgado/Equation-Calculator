from flask import *
import json

app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/api/data')
def cats():
    data = {"msg": "i am a cat"}
    return json.dumps(data)

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host="localhost")
