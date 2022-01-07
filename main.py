import random, string
from flask import Flask, render_template, request
import requests
import json
import os

app = Flask(
	__name__,
	template_folder='templates',
	static_folder='assets'
)

def ai(link, mainlink):
  link = f'{mainlink}/{link}'
  
  f = requests.get(link)
  
  return f.text

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

    output = ai(urll, "https://vishy-6.jfdkfsjfbskdf.repl.co/")

    if output == "invalid input":
      output = ai(urll, "https://vishy-2.jfdkfsjfbskdf.repl.co/")

    r = requests.get(urll, allow_redirects=True)

    im = open(f'assets/image.png', 'wb').write(r.content)

    print(output)

    return render_template(
		'index2.html',code=output,urll=urll)

    


if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
		port=random.randint(2000, 9000)
	)