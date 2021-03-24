from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import abort
import random
import math

app = Flask(__name__)


def rand():
    return math.ceil(random.random() * 100)


@app.route('/')
def index():
    # print('娃哈哈', request.headers)
    indexs = []
    r = rand()
    for _ in range(0, r):
        indexs.append(rand())
    return render_template('index.html', title=request.headers.get('User-Agent'), r=rand(), indexs=indexs)


@app.route('/user/<name>')
def user(name):
    if not name:
        abort(404)
    return render_template('index.html', title=name)


@app.route('/cookie/<act>')
def cookie(act):
    if act == 'set':
        name = 'sam_' + str(random.random())
        response = make_response(render_template('index.html', title='set cookie name ' + name))
        response.set_cookie('name', name)
        return response
    if act == 'get':
        name = request.cookies.get('name')
        if not name:
            name = 'null'
        return render_template('index.html', title='cookie name ' + name)


@app.route('/redirect')
def redirect_url():
    return redirect('http://www.google.com')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
