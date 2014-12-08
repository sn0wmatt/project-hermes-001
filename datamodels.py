class Chat(ndb.model):
    userA = ndb.StringProperty()
    userB = ndb.StringProperty()
    url = ndb.StringProperty()
    started = ndb.DateTimeProperty()

    def __init__(self):
        self.started = # Time of start -> Now.

class userA(ndb.model):
    """
        This class holds all of the data for "User A" in a more compact and easily accessable manner.
    """

    turn = False
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    posts = ndb.IntegerProperty()
    # All the rest of the shit needed.

class userB(ndb.model):
    """
        This class holds all of the data for "User B" in a more compact and easily accessable manner.
        More or less a clone of "User A" class.
    """

    turn = False
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    posts = ndb.IntegerProperty()
    # All the rest of the shit needed.
