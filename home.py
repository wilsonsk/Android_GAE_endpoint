from google.appengine.ext import ndb

class HomeModel(ndb.model.Model):
	userId = ndb.StringProperty()
	address = ndb.StringProperty()
	headline = ndb.StringProperty()
	squareFeet = ndb.IntegerProperty()
	price = ndb.IntegerProperty()

