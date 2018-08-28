from flask import Flask, session
from checker import check_logged_in
app=Flask(__name__)
app.secret_key='youwillnevergessmysecretkey'
@app.route('/')
def hello()->str:
    return 'hello from the simple webapp'
@app.route('/page1')
@check_logged_in
def page1()->str:
    return 'this is page 1'
@app.route('/page2')
@check_logged_in
def page2()->str:
    return 'this is page 2'
@app.route('/page3')
@check_logged_in
def page3()->str:
    return 'this is page 3'
@app.route('/login')
def do_login()->str:
    session['logged_in'] = True
    return 'you are now logged in'

@app.route('/logout')
def do_logout()->str:
    session.pop('logged_in')
    return 'you are now logged out'

if __name__ == '__main__':
    app.run(debug=True)

