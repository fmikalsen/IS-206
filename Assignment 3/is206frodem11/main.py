import webapp2
import re
import os
import string
import jinja2

import birthday
import signup
import rot13
import blog
import util
import cookie


class MainPage(util.BaseHandler):
	def get(self):
		self.render('index.html')


app = webapp2.WSGIApplication([('/', MainPage),
				('/welcome', signup.WelcomeHandler),
				('/signup', signup.SignupHandler),
				('/birthday', birthday.BdayHandler),
				('/thanks', birthday.ThanksHandler),
				('/rot13', rot13.Rot13Handler),
				('/blog', blog.BlogHandler),
				('/blog/newpost', blog.NewpostHandler),
				('/blog/(\d+)', blog.PermaLink),
				('/blog/signup', cookie.SignupHandler),
				('/blog/welcome', cookie.WelcomeHandler),
				('/blog/login', cookie.LoginHandler),
				('/blog/logout', cookie.LogoutHandler)
				], debug=True)
