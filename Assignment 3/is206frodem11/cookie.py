import util
import webapp2
import os
import re
import hmac
import main
import jinja2
from google.appengine.ext import db

class User(db.Model):
        username = db.StringProperty(required = True)
        password = db.StringProperty(required = True)
        email = db.StringProperty(required = False)


class SignupHandler(util.BaseHandler):
        def get(self):
                user_id = self.request.cookies.get('user_id')
                if user_id:
                        secure = util.check_secure_val(user_id) #checks that the cookie is secure, hashed
                        if secure:
                                self.redirect("/blog/welcome")
                else:
                        self.render("register.html")
                #self.render("Registration.html",username=b.username,password=b.password,email=b.email)
        def post(self):
                user_username = self.request.get('username')
                user_password = self.request.get('password')
                user_verify = self.request.get('verify')
                user_email = self.request.get('email')
                
                errors = util.check_signup(user_username, user_password, user_verify, user_email)
                if errors:
                        self.render("register.html",error = errors[0],error2 = errors[1],error3 = errors[2],error4 = errors[3],username = user_username)
                else:
                        u = User(username = user_username, password = util.make_pw_hash(user_username,user_password), email = user_email)
                        u.put()
                        user_id = u.key().id()
                        new_cookie_val = util.make_secure_val(str(user_id))
                        self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % new_cookie_val)
                        self.redirect("/blog/welcome")

class WelcomeHandler(util.BaseHandler):
	def get(self):
		user_id = self.request.cookies.get('user_id')
		secure = util.check_secure_val(user_id)
		if secure:
			b = User.get_by_id (int(secure))
			self.render("welcome.html", b=b)
		else:
			self.redirect("/blog/signup")


class LoginHandler(util.BaseHandler):
	def get(self):
		user_id = self.request.cookies.get('user_id')
		if user_id:
			secure = util.check_secure_val(user_id)
			if secure:
				self.redirect("/blog/welcome")
		else:        
			self.render("login.html")
	def post(self):
		user_username = self.request.get('username')
		user_password = self.request.get('password')
		err1 = ""
		users = db.GqlQuery("SELECT * FROM User")
		user_exist = None
		for user in users:
			if util.valid_pw(user_username,user_password,user.password):
				user_exist = user
		if user_exist:
			user_id = user_exist.key().id()
			new_cookie_val = util.make_secure_val(str(user_id))
			self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % new_cookie_val)
			self.redirect("/blog/welcome")
		else:
			err1 = "Invalid login"
			self.render("login.html",error = err1)



class LogoutHandler(util.BaseHandler):
	def get(self):
		user_id = self.request.cookies.get('user_id')
		user_id = ""
		new_cookie_val = str(user_id)
		self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' %new_cookie_val)
		self.redirect("/blog/signup")








