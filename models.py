from google.appengine.ext import ndb

class Talk(ndb.Model):
    name = ndb.StringProperty()
    users = ndb.UserProperty(repeated=True)
    messages = ndb.JsonProperty(repeated=True)
    host = ndb.UserProperty()
