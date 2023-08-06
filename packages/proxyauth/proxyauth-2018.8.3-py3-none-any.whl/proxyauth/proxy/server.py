from datetime import timedelta

import inquirer
import redis
from flask import Flask, request, redirect, url_for, jsonify, current_app, session, Response
from flask_session import Session
from inquirer import themes

from proxyauth.auth.auth import auth, proxy_all, session_setup

app = Flask(__name__)

# app.config['SESSION_COOKIE_HTTPONLY'] = True

# proxy all 需要path参数
@proxy_all(app=app)
def proxy(path):
    return request.url.replace(':'+app.config.get('port'),
                               ':'+app.config.get('source_port'))

# @app.route('/1')
# @auth(app=app)
# def proxy():
#     return request.url.replace(':'+app.config.get('port'),
#                                ':'+app.config.get('source_port'))

# @app.route('/1')
# @auth(app=app)
# def proxy1():
#     print('*'*400)
#     return '127.0.0.1:7003/1'

@app.route('/error', methods=['GET'])
def cookie():
    return 'error'

@app.route('/session', methods=['GET'])
def setup():
    return session_setup()

if __name__ == '__main__':
    questions = [
        inquirer.Text('host', message="host?", default='0.0.0.0'),
        inquirer.Text('port', message="port?", default='7001'),
        inquirer.Text('secret', message="secret?", default='damengproxy123'),
        inquirer.Text('redirect', message="redirect url?", default='http://127.0.0.1:7000'),
        inquirer.Text('auth', message="auth url?", default='http://127.0.0.1:7000'),
        inquirer.Text('source', message="source port?", default='7002'),
        inquirer.Text('lifetime', message="session lifetime?", default='100'),
        inquirer.Text('cipher', message="cipher?", default='helloworld'),
    ]

    config = inquirer.prompt(questions, theme=themes.GreenPassion())

    app.config['redirect'] = config.get('redirect')
    app.config['auth'] = config.get('auth')
    app.config['SECRET_KEY'] = config.get('secret')
    app.config['port'] = config.get('port')
    app.config['source_port'] = config.get('source')
    lifetime = config.get('lifetime')



    app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
    app.config['SESSION_PERMANENT'] = True  # 如果设置为True，则关闭浏览器session就失效。
    app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
    app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='soc_cache')

    Session(app)

    if lifetime:
        app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=int(lifetime))
    app.run(
        host=config.get('host', '127.0.0.1'),
        port=int(config.get('port', '7001'))
    )

