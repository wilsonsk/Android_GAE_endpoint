from flask import request
from flask_restful import Resource
from google.appengine.ext import ndb

import json
from utils import jsonDumps, getObj

from home import HomeModel

class Home(Resource):
	def get(self):
		home = HomeModel.query(HomeModel.homeId == request.args.get("homeId")).fetch()
		if home:				
			home_dict = {'Home': []}
			for home in home:
				home_data = home.to_dict()
				home_dict['Home'].append(home_data)	

			return json.dumps(home_dict)
		
		else:
			homes = HomeModel.query(HomeModel.userId == request.args.get("userId")).fetch()
			home_dicts = {'Homes':[]}
			for home in homes:
				id = home.key.urlsafe()
				home_data = home.to_dict()
				home_data['self'] = '/homes/' + id 
				home_data['id'] = id
				home_dicts['Homes'].append(home_data)
		
			return json.dumps(home_dicts)

	def post(self):	
		newHome = HomeModel()
		newHome.homeId = request.json["homeId"]
		newHome.userId = request.json["userId"]
		newHome.address = request.json["address"]
		newHome.headline = request.json["headline"]
		newHome.squareFeet = int(request.json["squareFeet"])
		newHome.price = int(request.json["price"])
		newHome.put()
		return "Data was POSTed"

	
	def patch(self):	
		home = HomeModel.query(HomeModel.homeId == request.args.get("homeId")).fetch()

		if home:
			home_dict = {'Home': []}
			for home in home:
				key = home.key.urlsafe()
			h = getObj(key)
			return request.json["squareFeet"]	
#			temp = request.json["address"]				
#			if temp is not "": 
#				h.address = request.json["address"]
#	
#			temp = request.json["headline"]				
#			if temp is not "": 
#				h.headline = request.json["headline"]
#
#			temp = request.json["squareFeet"]				
#			if temp is not "": 
#				h.squareFeet = int(request.json["squareFeet"])
#
#			temp = request.json["price"]				
#			if temp is not "": 
#				h.price = int(request.json["price"])
#
#			h.put()
#			return "PATCH SUCCESS"

		
	
		else:
			return "Patch Error: no user id"

	def delete(self):
		home = HomeModel.query(HomeModel.homeId == request.args.get("homeId")).fetch()
		return 'Hello DELETE home'
