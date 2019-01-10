# -*- coding: UTF-8 -*-
import os
import string
import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'



@app.route('/hello')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!  random:'+get_random_str(12)




#获取随机字符串
def get_random_str(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))




if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
