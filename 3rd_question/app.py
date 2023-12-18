# Develop a Flask app that uses URL parameters to display dynamic content.
from flask import Flask ,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return f"Welcome to my home page"

@app.route('/index/<name>')
def dynamic_content(name):
    return render_template('index.html',name=name)


if __name__=="__main__":
    app.run(host="0.0.0.0")