from google.appengine.ext import ndb

class Talk(ndb.Model):
    id = ndb.IntegerProperty()
    users = ndb.UserProperty(repeated='true')
    messages = ndb.JsonProperty(repeated='true')
    host = ndb.UserProperty()
