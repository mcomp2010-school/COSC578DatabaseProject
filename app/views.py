from flask import render_template
from flask import flash
from flask import redirect
from flask import session
from flask import url_for
from flask import request
from flask import g

from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import current_user
from flask.ext.login import login_required

from app import app
from app import db
from app import lm
from app import forms
from app import models
#from models import Resources

@app.before_request
def before_request():
    g.user = current_user
    
@lm.user_loader
def load_user(id):
    return models.Resources.query.get(int(id))

@app.route('/')
def index():
    u = models.Resources(firstName='john', lastName='john@email.com')
    db.session.add(u)
    db.session.commit()


    return render_template('index.html',
                           title='Home',
                           user=models.Resources.query.all())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
    