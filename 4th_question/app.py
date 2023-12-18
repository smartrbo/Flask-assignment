# 4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask , render_template ,request
app=Flask(__name__)

@app.route('/')
def input_form():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    username = request.form['username']
    password = request.form['password']
    return f'Thank you, {username}, and {password} , and for submitting the form!'


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8003)