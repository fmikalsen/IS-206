import webapp2
import re

form="""
<html>
    <body>
        <h1>Signup</h1>
        <form method="post">
            <table>
                <tr>
                    <td>Username</td>
                    <td><input type="text" name="username" value="%(username)s"></td>
                    <td>%(error_username)s</td>
                </tr>
                <tr>
                    <td>Password</td>
                    <td><input type="password" name="password" value=""></td>
                    <td>%(error_password)s</td>
                </tr>
                <tr>
                    <td>Verify password</td>
                    <td><input type="password" name="verify" value=""></td>
                    <td>%(error_verify)s</td>
                </tr>
                <tr>
                    <td>e-mail (optional)</td>
                    <td><input type="text" name="email" value="%(email)s"></td>
                    <td>%(error_email)s</td>
                </tr>
            </table>
        <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

welcome = """
<html>
    <body>
        <h1>Welcome, %(username)s</h1>
    </body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return EMAIL_RE.match(email)


class SignupHandler(webapp2.RequestHandler):

    def write_in(self, username="", password="", verify="", email="", error_username="", error_password="", error_verify="", error_email=""):
        self.response.out.write(form % {"username": username,
                                        "email": email,
                                        "error_username": error_username,
                                        "error_password": error_password,
                                        "error_verify": error_verify,
                                        "error_email": error_email})

    def get(self):
        self.write_in()

    def post(self):
        have_error = False
        email = ""
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username, email = email)

        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True
        if email != "":
            if not valid_email(email):
                params['error_email'] = "That's not a valid email."
                have_error = True

        if have_error:
            self.write_in(**params)
        else:
            self.redirect("/welcome?username=" + username)


class WelcomeHandler(webapp2.RequestHandler):

    def get(self):
        username = self.request.get('username')
        self.response.out.write(welcome % {"username": username})
