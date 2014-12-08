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

@app.route('/', methods=['GET','POST'])
def index():
    print(request.method == 'GET')
    
    if(request.method == 'GET'):
        pass
    elif(request.method == 'POST'):
        u = models.Resource(firstName='john', lastName='john@email.com')
        # INSERT FIRST
        
        db.session.add(u)
        
        db.session.commit()
        
    return render_template('projects/projects.html',
                           title='Home',
                           user=models.Resource.query.all())


@app.route('/tasks', methods=['GET','POST'])
def tasks():
    return render_template('tasks/tasks.html',
                           title='Home')
    

@app.route('/resources', methods=['GET','POST'])
def resources():
    return render_template('/resources/resources.html',
                           title='Home')
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    
    form = forms.LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        print("Valid")
        
        
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
    