from flask import render_template, flash
from app.giturl_class.url_form import UrlForm
from app.giturl_class import bp
import json

@bp.route('/index', methods = ['GET', 'POST'])
def urlPage():
    form = UrlForm()
    citation = None
    installation = None
    invocation = None
    description = None
    if form.validate_on_submit():
        flash("Classifying data")

        with open('data/output.json') as json_file:
            data = json.load(json_file)
            citation = data['citation.sk']
            installation = data['installation.sk']
            invocation = data['invocation.sk']
            description = data['description.sk']

    return render_template('giturl_class/giturl.html',
                           form = form,
                           citation = citation,
                           installation = installation,
                           invocation = invocation,
                           description = description)


@bp.route('/about', methods = ['GET'])
def aboutPage():
    return render_template('aboutpage/aboutpage.html')


@bp.route('/help', methods = ['GET'])
def helpPage():
    return render_template('helppage/helppage.html')