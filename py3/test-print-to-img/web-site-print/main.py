from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import abort
import random
import math
import time
import print


app = Flask(__name__, static_url_path=None,
            static_folder='./uploads', static_host=None, template_folder='./templates')


def rand(lenNum=100):
    return math.ceil(random.random() * lenNum)


@app.route('/')
def index():
    # print('娃哈哈', request.headers)
    indexs = []
    r = rand()
    for _ in range(0, r):
        indexs.append(rand())
    return render_template('index.html', title=request.headers.get('User-Agent'), r=rand(), indexs=indexs)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    time_str = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    img = request.files.get('file')
    i1 = img.filename.rfind('.')
    i2 = len(img.filename)
    name_suffix = img.filename[i1:i2]
    file_path = 'uploads/'+time_str+'_'+str(rand(10000000))+name_suffix
    img.save(file_path)
    print.startPrint(file_path)
    return render_template('upload_result.html', img_url=file_path, img_name=img.filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
