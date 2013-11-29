import web
from TADA import map
from TADA import play

urls = (
	"/game", "GameEngine"
	"/", "index",
)


app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store, initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

render = web.template.render('templates/', base="layout")


class index(object):
	def GET(self):
		return render.index()

	def POST(self):
		form = web.input(action=None)
		
		#Det er en bug her
		if sesion.room and form.action:
			session.room = session.room.go(form.action)

		web.seeother("/game")

if __name__ == "__main__":
	app.run()
