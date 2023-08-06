import base64
import hashlib
import urllib
from datetime import timedelta
from urllib.parse import urlsplit

import bcrypt
import redis as redis
from flask import Flask, request, redirect, jsonify, render_template, session
from flask_session import Session

from proxyauth.auth.auth import sign_hash, generate_token, valid, valid_hash, AESCipher
from proxyauth.auth.user_store import user_store

app = Flask(__name__)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        password = request.form['password']
        repassword = request.form['repassword']
        #检测注册时两次输入密码是否相同
        if password != repassword:
            return render_template('signup.html', errors=['password', 'repassword'])

        username = request.form['username']
        hashed_password = sign_hash(password)
        #
        #如果用户名已经存在
        store = user_store('auth_user', db='auth_user')
        elem = store.read(username)
        if elem:
            return render_template('signup.html', errors=['username'])

        #否则现实注册成功
        store.create(username, {'pwd': hashed_password})
        store.disconnect()
        return render_template('signuped.html', username=username, password=password)
    return render_template('signup.html')

@app.route('/auth', methods=['GET', 'POST'])
def index():
    redirect_url = request.args.get('redirect_url')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form.get('remember')
        token = generate_token(username, password)

        if remember:
            #默认的session在redirect时两边会清空，redis的session在redirect时两边都会设置
            session['remember'] = AESCipher().encrypt_b64(username+'.'+password)
        if valid(username, password):
            if redirect_url and redirect_url != 'None':
                decrpyt_url = AESCipher().decrypt_b64(redirect_url)
                sp_url = urlsplit(decrpyt_url)
                session_url = sp_url.scheme + '://'+ sp_url.netloc +'/session'
                return redirect(session_url+'?redirect_url='+redirect_url+'&token='+token)
            return 'hello no redirect'
        return 'hello invalid'

    remember = session.get('remember')
    if remember:
        remember = AESCipher().decrypt_b64(remember)
    return render_template('signin.html', redirect_url=redirect_url, remember=remember)


@app.route('/verify', methods=['POST'])
def verify():
    token = request.args.get('token')
    if token:
        token = base64.b64decode(token).decode('utf-8')
        hash_usr, hash_pwd = token.split('.')
        if valid_hash(hash_usr, hash_pwd):
            return jsonify({'valid': True})
    return jsonify({'valid': False})



app.config['SECRET_KEY'] = 'damengauth'
app.config['SESSION_COOKIE_HTTPONLY'] = True


app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='soc_cache')

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=int(20))

Session(app)



if __name__ == '__main__':
    app.run(port=7000)
