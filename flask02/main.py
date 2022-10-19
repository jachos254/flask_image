from flask import Flask, render_template, jsonify, request
from random import randint

app = Flask(__name__)

@app.route('/')
def index():

    if request.is_json:
        number = randint(1, 10)
        return jsonify({'number': number})
    return render_template("index.html")

if __name__ == "__main__":
    app.run()