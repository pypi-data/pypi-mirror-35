from datetime import timedelta

import inquirer
from flask import Flask, request, redirect, url_for, jsonify, current_app, session, Response
from inquirer import themes

from proxyauth.auth.auth import auth, proxy_all, session_setup

app = Flask(__name__)

# app.config['SESSION_COOKIE_HTTPONLY'] = True

@proxy_all(app=app, auth_url=app.config.get('auth'))
def proxy(path):
    return request.url.replace(':'+app.config.get('port'),
                               ':'+app.config.get('source_port'))


@app.route('/error', methods=['GET'])
def cookie():
    return 'error'

@app.route('/session', methods=['GET'])
def setup():
    print('session', '.......')
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
    ]

    config = inquirer.prompt(questions, theme=themes.GreenPassion())

    app.config['redirect'] = config.get('redirect')
    app.config['auth'] = config.get('auth')
    app.config['SECRET_KEY'] = config.get('secret')
    app.config['port'] = config.get('port')
    app.config['source_port'] = config.get('source')
    lifetime = config.get('lifetime')
    if lifetime:
        app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=int(lifetime))
    app.run(
        host=config.get('host', '127.0.0.1'),
        port=int(config.get('port', '7001'))
    )

