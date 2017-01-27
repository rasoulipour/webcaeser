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
import ceasar
import cgi


def page_builder(in_message):
    rotation_label = '<label>rotate by:</label>'
    message_label = '<label>message you want to encript:</label>'
    rotation_input = '<input type = "number" name = "rotation">'
    submit = '<input type="submit" />'
    textarea = '<textarea name="message">'+ in_message +'</textarea>'

    header = '<h1>Web Ceasar!</h1>'

    form = ('<form method="post">' + message_label
    + textarea + '<br>' + rotation_label + rotation_input
    + '<br>' + submit + '</form>')

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = page_builder("")
        self.response.write(content)

    def post(self):
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        incripted_message = ceasar.encrypt(message, rotation)
        escaped_message = cgi.escape(incripted_message)
        content = page_builder(escaped_message)
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
