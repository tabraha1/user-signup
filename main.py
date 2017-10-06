from flask import Flask, render_template, redirect, url_for, request
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '':
            error = 'Invalid Credentials. Please try again.'
        elif len(request.form['username']) < 3 or len(request.form['password']) < 3:
            error = 'Either username or password is too short.'
        elif len(request.form['username']) > 20 or len(request.form['password']) > 20:
            error = 'Either username or password is too short.'
        elif request.form['password'] != request.form['verify']:
            error = 'Password does not match.'
        elif re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", request.form['email']) == None:
            error = 'Not a valid email.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()