#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os

from google.appengine.api import users
from google.appengine.ext.webapp import template
from models import Talk

class ChatroomListHandler(webapp2.RequestHandler):
    """
        This is a temporarily named test handler
    """
    def render_template(self, template_name, values):
        path = os.path.join(os.path.dirname(__file__), "home", template_name)
        return template.render(path, values)

    def get(self):
        query = Talk.query()
        to_parse = list()
        for singular in query:
            f_q = {"talk_key": str(singular.key.id()), "name": singular.name}
            to_parse.append(f_q)
        template_string = {"query_results": to_parse}
        self.response.write(self.render_template("home.html", template_string))

class MainHandler(webapp2.RequestHandler):
    """
        This is the main handler.
    """

    def queryTalks(ID):
        q = Talk.all(keys_only=True)
        return q.filter('__key__ >', ID)

    def render_template(self, template_name, values):
        path = os.path.join(os.path.dirname(__file__), "html", template_name)
        return template.render(path, values)

    def get(self):
        # gets the user from the google users datastore.
        user = users.get_current_user()
        talk_key = self.request.get("talk_key")

        if not user:
            # if user is not logged in, log them in.
            self.redirect(users.create_login_url(self.request.uri))
            return
        if not talk_key:
            talk = Talk()
            talk.host = user
            talk.put()
            self.talk = talk
            talk_key = talk.key.id()
            self.redirect(str(self.request.url + "?talk_key=%i" % talk_key ))
        else:
            talk = Talk.get_by_id(long(self.request.get("talk_key")))

            if not user in talk.users:
                # Add user to users, allow to talk.
                talk.users.append(user)

        key_name = self.request.get("talk_key")
        template_things = {"id": key_name, "talk": talk}
        self.response.write(self.render_template("index.html", template_things))

    def post(self):
        user = users.get_current_user()

        sent_message = self.request.get("message_content")
        talk = Talk.get_by_id(long(self.request.get("talk_key")))
        message_package = {"author": str(user), "message": sent_message}
        talk.messages.append(message_package)
        talk.put()

        key_name = long(self.request.get("talk_key"))
        template_things = {"id": key_name, "talk": talk}
        self.response.write(self.render_template("index.html", template_things))

class RedirectHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/home")

app = webapp2.WSGIApplication([('/chatroom', MainHandler),
                                ('/home', ChatroomListHandler),
                                ('/', RedirectHandler)],
                              debug=True)
