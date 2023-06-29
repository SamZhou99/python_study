import json, datetime
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import abort

from VMail import VMail

app = Flask(__name__)


@app.route("/")
def index():
    return {"message": "api"}


@app.route("/email/<mail>", methods=["GET"])
def email(mail):
    if not mail:
        abort(404)
    vmail = VMail()
    temp = mail.split("@")
    domain = temp[1]
    name = temp[0]
    result = vmail.latestEmails(domain, name)
    return {"email": mail, "data": result}


@app.route("/sms-hook", methods=["GET"])
def sms_get():
    path = "./post.txt"
    f = open(path, "r")
    l = f.read().split("\n")
    l = l[:-1]
    f.close()
    a = []
    for d in l:
        d = json.loads(d)
        a.append(d)
    return {"get": a}


@app.route("/sms-hook", methods=["POST"])
def sms_post():
    d = dict(request.form)
    d.update({"ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")})
    txt = json.dumps(d)
    path = "./post.txt"
    f = open(path, "a")
    f.write(txt + "\n")
    f.close()
    return {"post": d}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
