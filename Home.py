from flask import request
from flask_restful import Resource
from google.appengine.ext import ndb

from home import HomeModel

class Home(Resource):
	def get(self):
		return HomeModel.query(ndb.GenericProperty("userId") == request.json["userId"]).get()
	
	def post(self):
		if(HomeModel.query(ndb.GenericProperty("userId") == request.json["userId"])):
			newHome = HomeModel()
			newHome.userId = request.json["userId"]
			newHome.address = request.json["address"]
			newHome.headline = request.json["headline"]
			newHome.squareFeet = int(request.json["squareFeet"])
			newHome.price = int(request.json["price"])
			newHome.put()
			return "Data was POSTed"

	def delete(self):
		return 'Hello DELETE home'
