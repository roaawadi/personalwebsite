from flask import Flask ,render_template
import random
app= Flask(__name__)

@app.route("/")
def index ():
	adjectives=["you are ugly" , "you are mean" , "you are beautifull" , "you have a great smile" , "your teeth are ugly"]
	return render_template("home.html",you=random.choice(adjectives))


@app.route("/home")
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

