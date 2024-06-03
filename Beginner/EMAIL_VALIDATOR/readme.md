# Email Validation Scripts

This repository contains three Python scripts for checking if an email address is valid. Each script does it in a different way:

## 1. CHECK_MAIL1.py

This script checks if an email address is valid using basic logic and string manipulation. It looks at things like:
- Making sure the email has at least 6 characters.
- The first character should be a lowercase letter.
- There should be only one "@" symbol.
- The email's domain should end with ".com" or ".edu".
- No spaces are allowed.
- The email shouldn't have any uppercase letters, except in the domain.

### Code:
```python

email = input("ENTER YOUR EMAIL ID : ")
k,j,d = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == "." ) ^ (email[-3] == "." ):
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i == "." or i == "@":
                        continue
                    else:
                        d=1
                if k == 1 or j == 1 or d == 1:
                    print(" Email not accepted ")
                else:
                    print(" email accepted ")
            else:
                print(" Email not accepted ")
        else:
            print(" Email not accepted , there should be @ in a Email ID and only one @ is allowed")
    else:
        print("  Email not accepted , first letter should not be capital ")
else:
    print(" Email not accepted , there should be more character that 6 ")

```

## 2. CHECK_MAIL2.py

This script uses a module called `re` to check if an email address is valid. It uses a special code pattern called a regular expression to do this. It looks at things like:
- The email's local part can have lowercase letters, digits, dots, and underscores.
- There should be only one "@" symbol.
- The domain part should have alphanumeric characters and end with a valid top-level domain (like ".com" or ".edu").

### Code:
```python
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input(" Enter your Email: ")

if re.search(email_condition, user_email):
    print(" Email accepted ")
else:
    print(' Email not Excepted .')
```

## 3. app.py

This script is a web application made with Flask. It lets you enter an email address in a web page, then it checks if it's valid or not using a regular expression. If the email is valid, it shows a message saying so. Otherwise, it shows an error message.

### Code:
```python
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

```

Feel free to use these scripts to check email addresses in your own projects. If you have any questions or ideas, feel free to ask!
