from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health-check')
def health_check():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
