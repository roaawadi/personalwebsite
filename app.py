from flask import Flask ,render_template , request
import random
#mport dataset
#db = dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")print(table.columns)

app= Flask(__name__)

@app.route("/hello" , methods= ["POST"])
def form_res():
	user_firstname=request.form["firstname"]
	user_lastname=request.form["lastname"]
	user_massage=request.form["massage"]
	return render_template ('form_data.html' , firstname = user_firstname , lastname = user_lastname , massage = user_massage )
	#able.insert(dict(firstname = user_firstname, lastname = user_lastname , massage = user_massage ))
	#contact=table.find_one(firstname ="apple")
	#return render_template('contact.html' , firstname = contact['firstname')
@app.route("/")
def load1_page():
 	return render_template("home.html")


@app.route("/about")
def load2_page():
 	return render_template("about.html")


@app.route("/contact")
def load3_page():
 	return render_template("contact.html")

if __name__ == "__main__":
   app.run()

