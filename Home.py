from flask import Flask, render_template
from flask_restful import Resource, Api

class Home(Resource):
	def get(self):
		return 'Hello GET home'
	
	def put(self):
		return 'Hello PUT home'

	def delete(self):
		return 'Hello DELETE home'
