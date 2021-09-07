from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=False)
