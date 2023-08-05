import base64
import functools

from flask import session, request, redirect, Response
import requests as req

from proxyauth.auth.user_store import user_store
from hashlib import blake2b
from hmac import compare_digest

SECRET_KEY = b'This program is maintained by dameng.'
AUTH_SIZE = 16

# 检测用户的有效性
def valid(usr, pwd):
    store = user_store('auth_user', db='auth_user')
    #sign_hash(usr)
    elem = store.read(usr)
    es = store.read_all()
    if elem:
        pwd_in_db = elem.get('pwd')
        hashed_pwd = sign_hash(pwd)
        return pwd_in_db == hashed_pwd
    return False

# 检测用户的有效性(密码已经经过hash处理)
def valid_hash(usr, hashed_pwd):
    store = user_store('auth_user', db='auth_user')
    elem = store.read(usr)
    if elem:
        pwd_in_db = elem.get('pwd')
        return pwd_in_db == hashed_pwd
    return False



#hash token
def sign_hash(token):
    h = blake2b(digest_size=AUTH_SIZE, key=SECRET_KEY)
    h.update(token.encode('utf-8'))
    return h.hexdigest()#.encode('utf-8')

#验证token与sig是否相符合
def verify_hash(token, sig):
    good_sig = sign_hash(token).encode('utf-8')
    return compare_digest(good_sig, sig)


#生成token
def generate_token(username, password):

    hashed_username = username#sign_hash(username)
    hashed_password = sign_hash(password)
    raw = hashed_username+'.'+hashed_password
    return base64.b64encode(raw.encode('utf-8')).decode('utf-8')

def _proxy_request(*args, **kwargs):
    eh = kwargs.get('headers')
    if eh:
        headers = {key: value for (key, value) in request.headers if key != 'Host'}
        headers.update(eh)
    else:
        headers = eh
    url = kwargs.get('url')

    resp = req.request(
        url=url,
        method=request.method,
        headers=headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    content = resp.content
    response = Response(resp.content, resp.status_code, headers)
    return response

def auth(auth_url=None):
    def dec(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            # url, method, headers, data, cookie = func(*args, **kwargs)
            url = func(*args, **kwargs)

            # token不存在时，重定向到auth_url
            # auth_url重定向时带着当前的url作为rediect_url, 相当于auth后再重定向回来
            token = session.get('token')
            if token is None:
                redirect_url = request.args.get('redirect_url', request.url)
                return redirect(auth_url+'/auth?redirect_url='+redirect_url)

            #token存在时,验证token
            resp = req.post(auth_url+'/verify?token='+token)
            if resp:
                data = resp.json()
                if data.get('valid'):
                    return _proxy_request(url=url, headers={'token': token})
            session.pop('token')
            return redirect('/error')
        return wrap
    return dec

def proxy_all(app=None, auth_url=None):
    def dec(func):
        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
        def wrap(*args, **kwargs):
            if app is None:
                raise Exception('app is None')
            url = auth(auth_url=auth_url)(func)
            return url(*args, **kwargs)
        return wrap
    return dec

def session_setup():
    token = request.args.get('token')
    if token:
        session['token'] = token
    redirect_url = request.args.get('redirect_url')
    return redirect(redirect_url)
