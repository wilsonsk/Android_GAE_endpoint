from flask import request
from flask_restful import Resource
from google.appengine.ext import ndb

import json
from utils import jsonDumps, getObj

from home import HomeModel

class Home(Resource):
	def get(self, userId=None, homeId=None):
		home = HomeModel.query(HomeModel.homeId == homeId).fetch()
		if home:				
			home_dict = {'Homes': []}
			for home in home:
				home_data = home.to_dict()
				home_dict['Homes'].append(home_data)	

			return json.dumps(home_dict)
       	
		else:
			homes = HomeModel.query(HomeModel.userId == userId).fetch()
			home_dicts = {'Homes':[]}
			for home in homes:
				id = home.key.urlsafe()
				home_data = home.to_dict()
				home_data['self'] = '/homes/' + id 
				home_data['id'] = id
				home_dicts['Homes'].append(home_data)
		
			return json.dumps(home_dicts)

	def post(self, userId=None, homeId=None):	
		newHome = HomeModel()
		newHome.homeId = request.json["homeId"]
		newHome.userId = userId
		newHome.address = request.json["address"]
		newHome.headline = request.json["headline"]
		newHome.squareFeet = int(request.json["squareFeet"])
		newHome.price = int(request.json["price"])
		newHome.put()
		return 'New home created. Refresh and log back in to see changes.'

	
	def patch(self, userId=None, homeId=None):	
		home = HomeModel.query(HomeModel.homeId == homeId).fetch()

		if home:
			home_dict = {'Home': []}
			for home in home:
				key = home.key.urlsafe()
			h = getObj(key)

			temp = request.json["address"]				
			if temp != "": 
				h.address = request.json["address"]
	
			temp = request.json["headline"]				
			if temp != "": 
				h.headline = request.json["headline"]

			temp = request.json["squareFeet"]				
			if temp != "": 
				h.squareFeet = int(request.json["squareFeet"])

			temp = request.json["price"]				
			if temp != "": 
				h.price = int(request.json["price"])

			h.put()
			return 'Home patched. Refresh and log back in to see changes.'

		
	
		else:
			return "Patch Error: home could not be found"

	def delete(self, userId=None, homeId=None):
		home = homeId
		if home:
			home = HomeModel.query(HomeModel.homeId == homeId).fetch()
			home_dict = {'Home': []}
			for home in home:
				key = home.key.urlsafe()
			h = getObj(key)
	
			h.key.delete()

			return 'Home removed. Refresh and log back in to see changes.'
