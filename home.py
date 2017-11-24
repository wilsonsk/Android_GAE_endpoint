from google.appengine.ext import ndb

class HomeModel(ndb.model.Model):
	homeId = ndb.StringProperty()
	userId = ndb.StringProperty()
	address = ndb.StringProperty()
	headline = ndb.StringProperty()
	squareFeet = ndb.IntegerProperty()
	price = ndb.IntegerProperty()

