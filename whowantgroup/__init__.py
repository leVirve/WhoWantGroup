import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
# from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.debug import DebuggedApplication

app = Flask('application', instance_relative_config=True)
app.config.from_pyfile('config.py')

if os.getenv('FLASK_CONF') == 'TEST':
    app.config.from_object('whowantgroup.settings.Testing')

else:
    app.config.from_object('whowantgroup.settings.Production')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

db = MongoEngine(app)

from whowantgroup import urls
