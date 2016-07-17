from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route("/")
def form():
	return render_template('form_submit.html')

@app.route("/hello/",methods=['POST'])
def hello():
	name = request.form['yourname']
	email = request.form['youremail']
	print "Form Submitted with Values" 
	print "Name"+name+"Email"+email
	return render_template('form_action.html',name=name,email=email)

@app.route("/admin",methods=['POST'])
def hi():
	name = request.form['yourname']
	email = request.form['yourmail']
	return "Kunchala Anil{{name}} email  {{email}}"

if __name__ == "__main__":
	app.run(debug = True,host='0.0.0.0')
