import requests
import json

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

github_api = 'https://api.github.com/users'

@app.route('/')
def index():
    users_data = requests.get(github_api)
    users = users_data.json()
    return render_template('index.html', users=users)

@app.route('/users/<string:user_name>')
def get_user(user_name):
    user_data = requests.get(f'{github_api}/{user_name}')

    user = user_data.json()
    return render_template('user.html', user=user)





if __name__ == '__main__':
    app.run(debug=True)