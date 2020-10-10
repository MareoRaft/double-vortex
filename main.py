################################# IMPORTS #####################################
import sys
from warnings import warn
import pdb

import tornado
from tornado.web import url # constructs a URLSpec for you
# handlers
from tornado.web import RequestHandler
from tornado.web import RedirectHandler
from tornado.web import StaticFileHandler
# other
from tornado.web import Application
from tornado.web import Finish

################################## MAIN #######################################


class StaticCachelessFileHandler(StaticFileHandler):


	def set_extra_headers(self, path):
		# Disable cache
		self.set_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')


class ExtensionHandler(RequestHandler):


	def prepare(self):
		self.redirect(self.request.uri + '.html')
		Finish()


class DefaultHandler(RequestHandler):


	def get(self):
		self.render('double-vortex.html')


def make_app():
	return Application(
		[
			# as well as serving static files, this server will redirect certain requests to appropriate ports
			url(r'^/?$', DefaultHandler, {}),
			url(r'^/([^.]*)$', ExtensionHandler, {}), # if something has no dot, we ASSUME they wanted the .html extension
			url(r'^/(.*)', StaticCachelessFileHandler, { "path": "." }), # captures anything at all, and serves it as a static file. simple!
		],
		# settings:
		debug = True,
	)

def make_app_and_start_listening():
	#enable_pretty_logging()
	application = make_app()
	application.listen(8000)
	# other stuff
	tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
	make_app_and_start_listening()
