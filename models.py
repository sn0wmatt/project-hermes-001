from google.appengine.ext import ndb

class Talk(ndb.Model):
    name = ndb.StringProperty()
    users = ndb.UserProperty(repeated='true')
    messages = ndb.JsonProperty(repeated='true')
    host = ndb.UserProperty()
