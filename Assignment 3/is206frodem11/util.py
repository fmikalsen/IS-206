import util
import webapp2
import os
import re
import hmac
import main
import jinja2
import random
import string
import hashlib

from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)





USER_RE = re.compile(r"^[a-zA-Z0-9_-]{4,20}$")
PASS_RE = re.compile(r"^.{6,20}$")
E_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


def checkPassword(password,verify):
        if password == verify:
                return password
        else:
                return None


def checkUsername(username):
        if " " in username:
                return False
        elif USER_RE.match(username):
                return True
        else:
                return False

def checkPassIs(password):
        if PASS_RE.match(password):
                return True
        else:
                return False

def checkEmail(email):
        if email != "":
                return E_RE.match(email)
        else:
                return True


def check_signup(user_username, user_password, user_verify, user_email):
        err1 = ""
        err2 = ""
        err3 = ""
        err4 = ""
        if checkPassword(user_password,user_verify) == None:
                err1 = "Your passwords didn't match."
        if checkUsername(user_username) == False:
                err2 = "That's not a valid username."
        if not checkEmail(user_email):
                err3 = "That's not a valid email."
        if checkPassIs(user_password) == False:
                err4 = "Thats not a valid password."
        if err1 =="" and err2 =="" and err3 =="" and err4 =="":
                return []
        else:
                return [err1,err2,err3,err4]


SECRET = 'imsosecret'


def make_salt():
        return ''.join(random.choice(string.letters) for x in xrange(5))


def make_pw_hash(name,pw,salt = None):
        if not salt:
                salt = make_salt()
        h = hashlib.sha256(name + pw + salt).hexdigest()
        return '%s,%s' % (h,salt)


def valid_pw(name,pw,h):
        salt = h.split(',')[1]
        return h == make_pw_hash(name,pw,salt)
        

def hash_str(s):
        return hmac.new(SECRET,s).hexdigest()


def make_secure_val(s):
        return "%s|%s" % (s,hash_str(s))


def check_secure_val(h):
        val = h.split('|')[0]
        if h == make_secure_val(val):
                return val
