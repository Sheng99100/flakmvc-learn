from flask import Flask, request, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	text = request.args.get('text')
	return render_template('home.html', text = text)

@app.route('/signin', methods=['GET'])
def signin():
	return render_template('signin.html')


@app.route('/user/', methods = ['POST']) 
@app.route('/user/<username>', methods = ['POST'])
def user(username=None):
	username = request.form['username']
	return render_template('user.html', username=username)
