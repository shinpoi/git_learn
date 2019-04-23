from flask import Flask, url_for, request, render_template, Markup, jsonify, abort, redirect
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
	#return render_template('404.html'), 403
	return render_template('404.html'), 404

@app.route("/")
def index():
	return redirect(url_for('login'))

@app.route("/app", methods=['GET'])
def hello():
	if request.method == 'GET':
		se = request.args.get('id', 'unkown')
		return render_template('hello.html', name=se)

@app.route("/cal", methods=['GET'])
def cal():
	n1 = request.args.get('n1', None)
	n2 = request.args.get('n2', None)
	if n1 and n2:
		return "%s + %s = %d" % (n1 ,n2, int(n1)+int(n2))
	else:	
		return "Please input n1 and n2"

@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		id_ = request.form['id']
		pw_ = request.form['pw']
		return jsonify({'id':id_, 'pw':pw_})
	else:
		abort(403)
		#return "Please input id and password"

with app.test_request_context():
	print(url_for('hello'))
	print(url_for('hello', para='n'))
	print(url_for('cal', n1=10, n2=20))
	print(url_for('static', filename='style.css'))
	print(Markup('<p>%s</p>') % '<h1>yahaha</h1>')

if __name__ == "__main__":
	app.run()

