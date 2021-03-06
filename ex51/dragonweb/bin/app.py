import web

urls = (
	"/hello", "index"
)

app = web.application(urls, globals())

render = web.template.render("templates/", base="layout")

class index(object):
	def GET(self):
		return render.index()

	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.foo(greeting = greeting)

if __name__ == "__main__":
	app.run()
