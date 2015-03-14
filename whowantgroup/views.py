
from flask import render_template, request, abort, redirect
from jinja2 import TemplateNotFound

from whowantgroup import app, model, forms

def pjax(template):
    """Test whether the request was with PJAX or not."""
    if "X-PJAX" in request.headers:
        return render_template(template)
    return render_template("base.html", template=template)


def show_page(page):
    try:
        return render_template('base.html', content_template='%s.html' % page)
    except TemplateNotFound:
        abort(404)


def add_ac():
    form = forms.ActivityForm()
    if request.method == 'POST' and form.validate():
        # do something
        redirect('done')
    return render_template('t_add_ac.html', form=form)

activities = {
    '2517' :{
        'title': '我難過魯魯團',
        'date': '2015/03/25',
        'place': 'NTHU 台達館'
    },
    '2501': {
        'title': '活動二',
        'date': '2015/03/31',
        'place': 'NTHU 成功湖'
    },
    '2521': {
        'title': '活動三',
        'date': '2015/04/01',
        'place': 'NCTU'
    },
    '2511': {
        'title': '台達歡樂派',
        'date': '2015-03-31',
        'place': '台達館'
    },
}


def show_allactivity():
    return render_template('base.html',
                           content_template='activity.html',
                           activities=activities)


def show_activity(aid):
    app.logger.debug(aid)
    return render_template('base.html',
                           content_template='activity-group.html',
                           activity=activities[aid])

def hi():
    return 'hi'