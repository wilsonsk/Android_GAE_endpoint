""" server.py: top level module for the Flask application """

from Flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(err):
	return 'Sorry, nothing here.', 404

@errorhandler(500)
def application_error(err):
	return 'Sorry, server error.', 500

@app.route('/')
def landing():
	return 'Hello CS496'	

if __name__ == "__main__":
	app.run(debug=True)
