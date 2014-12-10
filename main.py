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

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, template_name, folder, values):
        path = os.path.join(os.path.dirname(__file__), folder, template_name)
        return template.render(path, values)


class ChatroomListHandler(BaseHandler):
    """
        This is a temporarily named test handler
    """
    def get(self):
        query = Talk.query()
        to_parse = list()
        for singular in query:
            f_q = {"talk_key": str(singular.key.id()), "name": singular.name}
            to_parse.append(f_q)
        template_string = {"query_results": to_parse}
        self.response.write(self.render_template("home.html", "home", template_string))

class MainHandler(BaseHandler):
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
        template_things = {"id": key_name, "talk": talk, "user": user}
        self.response.write(self.render_template("index.html", "html", template_things))
        self.response.write("Name: %s" % talk)

    def post(self):
        user = users.get_current_user()

        sent_message = self.request.get("message_content")
        talk = Talk.get_by_id(long(self.request.get("talk_key")))
        message_package = {"author": str(user), "message": sent_message}
        talk.messages.append(message_package)
        talk.put()

        key_name = long(self.request.get("talk_key"))
        template_things = {"id": key_name, "talk": talk}
        self.response.write(self.render_template("index.html", "html", template_things))

class RedirectHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/home")

class ChatroomRenameHandler(BaseHandler):
    talk_key = None
    def get(self):
        self.talk_key = self.request.get("talk_key")
        template_values = {"talk": Talk.get_by_id(long(self.talk_key)), "user": users.get_current_user(), "id": self.talk_key}
        self.response.write(self.render_template("chatroomRename.html", "chatroomRename", template_values))

    def post(self):
        name = self.request.get("name")
        talk_key = self.request.get("talk_key")
        talk = Talk.get_by_id(long(talk_key))
        talk.name = str(name)
        talk.put()
        self.redirect("chatroom?talk_key=%s&name=%s" % (str(talk_key), str(name)))

app = webapp2.WSGIApplication([('/chatroom', MainHandler),
                                ('/chatroomRename', ChatroomRenameHandler),
                                ('/home', ChatroomListHandler),
                                ('/', RedirectHandler)],
                              debug=True)
