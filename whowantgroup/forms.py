
from flask.ext.mongoengine.wtf import model_form
from whowantgroup import model

ActivityForm = model_form(model.Activity)