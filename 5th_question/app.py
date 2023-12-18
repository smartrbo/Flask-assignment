
# 5. Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'yuks123'  

@app.route('/')
def input_form():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    username = request.form['username']
    session['username'] = username  
    return redirect(url_for('display_data'))

@app.route('/display_data')
def display_data():
    username = session.get('username', 'Guest') 
    return f'Hello, {username}! This is your personalized page.'

@app.route('/logout')
def logout():
    session.pop('username', None)  
    return redirect(url_for('input_form'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
