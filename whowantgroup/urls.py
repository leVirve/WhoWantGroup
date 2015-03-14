
from whowantgroup import app
from whowantgroup import views

app.add_url_rule('/', view_func=views.hi)
app.add_url_rule('/add_ac', view_func=views.add_ac)
app.add_url_rule('/activity', view_func=views.show_allactivity)
app.add_url_rule('/activity/<aid>', view_func=views.show_activity)
app.add_url_rule('/<page>', view_func=views.show_page)
