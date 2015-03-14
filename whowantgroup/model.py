
from whowantgroup import db


class Activity(db.Document):
    title = db.StringField(required=True)
    date = db.DateTimeField()
    place = db.StringField()

