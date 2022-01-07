import random, string
from flask import Flask, render_template, request
import requests
import json
import os

#https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png

app = Flask(
	__name__,
	template_folder='templates',
	static_folder='assets'
)

@app.route('/')
def base_page():
	random_num = random.randint(1, 100000)
	return render_template(
		'index.html',
		random_number=random_num
	)

@app.route('/identify', methods = ["POST"])
def sendBots():

    urll = request.form['invitecode']

    token = "ZHZvbnRlLm1pbGlhbm9AaWNpbmdydWxlLmNvbQ==.ddeea093ca55abeca1947f7c90246cb71e92739fb3e3522c6d976236feea"

    data = {'url': urll, 'token': token}

    url = "https://aipokedex.com/getPoke"

    x = requests.post(url, data=data)

    y = json.loads(x.text)

    code = y["predictions"][0]["name"]

    r = requests.get(urll, allow_redirects=True)

    im = open(f'assets/image.png', 'wb').write(r.content)

    return render_template(
		'index2.html',code=code,urll=urll)

    


if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		port=random.randint(2000, 9000)
	)