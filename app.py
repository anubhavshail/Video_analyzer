for flask import Flask, render_template, response

app = Flask(__name__)

@app.route('/')
def index:
    return render_template('intex.html')

