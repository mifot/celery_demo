import config
import delegate
import logging
from flask import make_response, jsonify

app = config.app
logging.basicConfig(level=logging.INFO)


@app.route('/<name>')
def process(name):
    delegate.reverse(name)
    return 'done'


@app.route('/add/<a>')
def add(a):
    z = delegate.add(a)
    make_response(jsonify(z), 200)


if __name__ == '__main__':
    app.run(debug=True)
