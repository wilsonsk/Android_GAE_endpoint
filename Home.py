from flask import request
from flask_restful import Resource
from google.appengine.ext import ndb

import json
from utils import jsonDumps, getObj

from home import HomeModel

class Home(Resource):
	def get(self):
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
		home = request.args.get("id")
		if home:				
			
			return home
		
		else:
			newHome = HomeModel()
			newHome.homeId = request.json["homeId"]
			newHome.userId = request.json["userId"]
			newHome.address = request.json["address"]
			newHome.headline = request.json["headline"]
			newHome.squareFeet = int(request.json["squareFeet"])
			newHome.price = int(request.json["price"])
			newHome.put()
			return "Data was POSTed"

	def delete(self):
		return 'Hello DELETE home'
