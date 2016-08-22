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
import cgi

caesar_form = """
<!DOCTYPE html>

<html>
    <head>
        <title>Caesar Assignment 3(1) LCWF109</title>
        </head>

<body>
    <h2>Enter your text into Caesar:</h2>
    <form method="post">
        <textarea name="text"
                 style="height: 150px; width: 400px;">%s</textarea>
    <br>
    <input type = "submit">
    </form>

</body>

</html>
"""

class Caesar(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(caesar_form%txt)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
