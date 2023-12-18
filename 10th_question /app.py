# Design a Flask app with proper error handling for 404 and 500 errors.

from flask import Flask ,render_template

app=Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('connect.html'), 500


@app.route('/')
def home():
    return 'Welcome to the Flask App!'

@app.route('/not_found')
def not_found():
    abort(404)

@app.route('/internal_server_error')
def internal_server_error_route():
    1 / 0

if __name__=="__main__":
    app.run(host='0.0.0.0')