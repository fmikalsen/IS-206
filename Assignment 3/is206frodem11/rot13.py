import webapp2
import cgi

def escape_html(s):
	return cgi.escape(s, quote = True)

form = """
<form method="post">
	<h2>ROT13:</h2>
	<textarea name='text' style='height: 169px; width: 412px; margin: 0px;'>%(rot)s</textarea>
	<br>
	<input type = 'submit' value='translate'>
</form>
"""

abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rot13(s):
	words = ''
	if s:
		for i in s:
			if i not in abc:
				words += i
			else:
				current_pos = abc.find(i)
				words += abc[current_pos + 13]
		return words

class Rot13Handler(webapp2.RequestHandler):
	def write_form(self,rot=''):
		self.response.out.write(form %{'rot': escape_html(rot)})

	def get(self):
		self.write_form()

	def post(self):
		convert = rot13(self.request.get('text'))
		self.write_form(convert)
