from flask import request
from flask_restful import Resource
from google.appengine.ext import ndb

from home import HomeModel

class Home(Resource):
	def get(self):
		return 'Hello GET home'
	
	def post(self):
		newHome = HomeModel()
		newHome.userId = request.json["userId"]
		newHome.address = request.json["address"]
		newHome.headline = request.json["headline"]
		newHome.squareFeet = int(request.json["squareFeet"])
		newHome.price = int(request.json["price"])
		newHome.put()
		return request.json

	def delete(self):
		return 'Hello DELETE home'
