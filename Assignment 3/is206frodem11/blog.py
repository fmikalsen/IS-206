import util
import webapp2
import os

from google.appengine.ext import db


class Post(db.Model):
	subject = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)


class BlogHandler(util.BaseHandler):
	def render_blog(self, subject="", content="", error=""):
		posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
	
		self.render("blog.html", posts = posts)

	def get(self):
		self.render_blog()

class NewpostHandler(util.BaseHandler):
	def render_newpost(self, subject="", content="", error=""):
		self.render("newpost.html",subject=subject,content=content,error=error)

	def get(self):
		self.render_newpost()


	def post(self):
		subject = self.request.get("subject")
		content = self.request.get("content")

		if subject and content:
			p = Post(subject = subject, content = content)
			p.put()

			self.redirect("/blog/%d" % p.key().id())
		else:
			error = "Need both subject and content."
			self.render_newpost(subject, content, error)

class PermaLink(util.BaseHandler):
	def render_perma(self, p=""):
		self.render("permalink.html", p=p)

	def get(self, post_id):
		p = Post.get_by_id (int(post_id));
		self.render_perma(p)





















