import os
import dotenv

dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

import logging
import tornado.web
import tornado.ioloop
import tornado.autoreload
from tornado.options import define, options, parse_command_line

import routes
import groupme
import settings

logger = logging.getLogger(__name__)


application = tornado.web.Application(routes.ROUTES, **settings.SETTINGS)

define(
	'port',
	help='The port that this instance of the server should listen on',
	default='8080',
	type=int,
)

if __name__ == '__main__':
	parse_command_line()
	tornado.autoreload.start()

	application.listen(options.port)
	logger.info('Started listening on port %s', options.port)
	groupme.get_bot_group(settings.BOT_ID)

	tornado.ioloop.IOLoop.instance().start()
