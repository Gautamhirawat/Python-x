from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email_condition = r'^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,}$'
    user_email = request.form['user_email']

    if re.search(email_condition, user_email):
        return "Email accepted"
    else:
        return "Email not accepted"

if __name__ == '__main__':
    app.run(debug=True)
