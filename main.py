from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['DEBUG'] = True

def valid_login(name):
    if (name != "") and len(name) > 3 and len(name) < 20:
        return True
    else:
        return False

def valid_password(password):
    if password != "" and len(password) > 3 and len(password) < 20:
        return True
    else:
        return False

def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def login():
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    if request.method == 'POST':
        if not valid_login(request.form['username']): 
            username_error='Invalid username'
        if not valid_password(request.form['password']):
            password_error='Invalid password'
        if not request.form['password'] == request.form['verify']:
            verify_error='Passwords do no match'
        if not is_valid_email(request.form['email']):
            email_error='Email invalid'
    return render_template('login.html', username_error=username_error, password_error=password_error, verify_error=verify_error,email_error=email_error)

if __name__ == '__main__':
    app.run()