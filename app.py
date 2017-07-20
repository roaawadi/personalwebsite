from flask import Flask ,render_template , request
import random
app= Flask(__name__)

@app.route("/hello" , methods= ["POST"])
def form_res():
	user_firstname=request.form["firstname"]
	user_lastname=request.form["lastname"]
	user_massage=request.form["massage"]
	return render_template('form_data.html',firstname=user_firstname , lastname=user_lastname , massage=user_massage)

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

