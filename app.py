# Import dependencies
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)


# Homepage
@app.route("/")
def homepage():
	return render_template("index.html")


# Run application
if __name__ == "__main__":
	app.run(debug=True, port=8000)
