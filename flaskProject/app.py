from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)
users = [{"username": "Gleb"}]

users_list = [{'username': 'JPetrov', 'name': 'John', 'surname': 'Petrov', 'age': 19},
              {'username': 'AIvanov', 'name': 'Alex', 'surname': 'Ivanov', 'age': 21}]


@app.route("/", methods=['post', 'get'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')

        new_user = {'username': f'{name[0]+surname}', 'name': name, 'surname': surname, 'age': 21}

        users_list.append(new_user)
        # return '{} {}'.format(name, surname)
    return render_template("index.html",
                           time=datetime.datetime.now().replace(microsecond=False),
                           users=users_list)


if __name__ == '__main__':
    app.run(debug=True)
