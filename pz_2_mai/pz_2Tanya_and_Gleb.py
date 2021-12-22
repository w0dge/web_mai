from flask import Flask
from flask import request, make_response, redirect, abort
app = Flask(__name__)


users = [{'username': 'vvodge', 'name': 'Glebushka', 'surname': 'Bokun', 'age': 50},
         {'username': 'zotova.__', 'name': 'Tanyusha', 'surname': 'Zotova', 'age': 19}]
localhost = 'http://127.0.0.1:5000'


@app.route('/')
def index():
    return redirect(f'{localhost}/users')


@app.route('/users')
def user():
    data = ''
    for i in users:
        data += "<h1><a href=%s/users/%s>%s</a></h1>" % (localhost, i['username'], i['username'])
        data += '\n'
    return data


@app.route('/users/<username>')
def user_name(username):
    for i in users:
        if i['username'] == username:
            return f'<h2>{i}</h2>'
    return abort(404)


if __name__ == '__main__':
    app.run(debug=True)
