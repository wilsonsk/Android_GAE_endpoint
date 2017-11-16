""" server.py: top level module for the Flask application """

from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) 

@app.errorhandler(404)
def page_not_found(err):
	return 'Sorry, nothing here.', 404

@app.errorhandler(500)
def application_error(err):
	return 'Sorry, server error.', 500

@app.route('/')
def landing():
	return 'Hello CS496'	

""" REST API ROUTERS """
class Houses(Resource):
	def get(self):
		return 'Hello GET houses'

	def delete(self):
		return 'Hello DELETE houses'

class Home(Resource):
	def get(self):
		return 'Hello GET home'
	
	def put(self):
		return 'Hello PUT home'

	def delete(self):
		return 'Hello DELETE home'
	

api.add_resource(Houses, '/houses')
api.add_resource(Home, '/home')

if __name__ == "__main__":
	app.run(debug=True)
