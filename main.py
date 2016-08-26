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
from caesar1 import encrypt

# issue with both caesar.py and directory named caesar for import????maybe rename caesar1.py
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
                 style="height: 150px; width: 400px;">%(txt)s</textarea>
    <div>
        <label> ...and rotate by:
        <input type = "number" name = "rot" value = "%(rot_num)s"</div>

            </label>

    <br>
    <input type = "submit">
    </form>



</body>

</html>
"""
#/label at end of input type?for = "rot">    <p class = "error"></p> input type = "text"
#value for textarea %(txt)s?
#just make a function for htmlescape = cgi.escape(s, quote = True)?example Uda redirect
def escape_html(s):
    return cgi.escape(s, quote = True)

class CaesarHandler(webapp2.RequestHandler):
    def write_form(self, txt="", rot_num=""):
        #txt= cgi.escape(txt, quote = True)
        self.response.out.write(caesar_form % {"txt" : txt, "rot_num": rot_num})

    def get(self):
        self.write_form()



    def post(self):
        txt = escape_html(self.request.get("txt"))
        #txt = cgi.escape(self.request.get("txt"), quote = True)
        rot_num = self.request.get("rot_num")
        #rot_txt = encrypt(txt,int(rot_num))
        rot_txt = encrypt(txt, rot_num)
        self.write_form(rot_txt, rot_num)
        #self.write_form(rot_txt, rot_num)
#just rot_txt in return



app = webapp2.WSGIApplication([
    ('/', CaesarHandler)
], debug=True)
