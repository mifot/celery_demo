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
    result = delegate.add(a)
    return make_response(jsonify(result), 200)


@app.route('/times/<a>')
def add(a):
    result = delegate.times(a)
    return make_response(jsonify(result), 200)


if __name__ == '__main__':
    app.run(debug=True)
