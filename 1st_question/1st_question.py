#Create a Flask app that displays "Hello, World!" on the homepage.
from flask import Flask , request
app=Flask(__name__)

@app.route('/app')
def Hello_world_print():
    return f"Hello, World!"

if __name__=="__main__":
    app.run(host="0.0.0.0")