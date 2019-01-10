from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)


@app.route('/')
def indexController():
    return '''
    <h1>Hello World !</h1>
    <p>%s</p>
    ''' % request.headers.get('User-Agent')


@app.route('/user/<name>')
def user(name):
    if not name:
        abort(404)
    return '<h1>My name is %s</h1>' % name


@app.route('/cookie/<act>')
def cookieController(act):
    if act == 'show':
        response = make_response('<h1>show!</h1>')
        return response
    if act == 'set':
        response = make_response('<h1>set!</h1>')
        response.set_cookie('test_cookie', '123')
        return response


@app.route('/redirect')
def redirectController():
    return redirect('http://www.google.com')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)
