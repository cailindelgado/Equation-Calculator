from flask import *
import json
# import main

app = Flask(__name__, static_folder='../static', static_url_path='/')

@app.route('/derivative', methods=['POST'])
def handle():
    data = request.json
    print(data)
    # eqnJSON = {"eqn": "Equation recieved" + eqn}
    return jsonify({"ans": "2"})

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host="localhost")
