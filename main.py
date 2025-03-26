from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze")
def analyze():
    return render_template("analyzer.html")

if __name__ == "__main__":
    app.run(debug=True)
