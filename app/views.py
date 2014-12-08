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
from wtforms.form import FormMeta
#from models import Resources

@app.before_request
def before_request():
    g.user = current_user
    
@lm.user_loader
def load_user(id):
    return models.Resources.query.get(int(id))

##
# PROJECT
##
@app.route('/', methods=['GET'])
def index():
    projects = models.Project.query.all()
    
    return render_template('/project/index.html',
                           title='Home',
                           projects=projects)

@app.route('/project/<id>',methods=['GET','POST'])
def edit_project(id):
    edit = request.args.get('edit') is not None
    project = models.Project.query.get(int(id))
    form = None
    
    if request.method == 'GET':
        form = forms.ProjectForm(obj=project)
    elif request.method == 'POST':
        form = forms.ProjectForm()
        
    if form.validate_on_submit() and request.method == 'POST':
            form.populate_obj(project)
            db.session.commit()
            return redirect("/")
    
    if edit:
        button = "Update Resource"
    else: 
        button = ""
        
    return render_template('/project/new.html',
                       form=form,
                       url='/project/'+id+"?edit",
                       button=button)
  
@app.route('/project/new',methods=['GET','POST'])
def show_new_project():
    form = forms.ProjectForm()
    if form.validate_on_submit():
        project = models.Project()
        form.populate_obj(project)
        db.session.add(project)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('project/new.html',
                               form=form,
                               button="Add New Project")

##
# Task
##
@app.route('/task', methods=['GET'])
def task():
    tasks = models.Task.query.all()
    return render_template('/task/index.html',
                           title='Home',
                           tasks=tasks)

@app.route('/task/<id>',methods=['GET','POST'])
def edit_task(id):
    edit = request.args.get('edit') is not None
    resource = models.Task.query.get(int(id))
    form = None
    
    if request.method == 'GET':
        form = forms.TaskForm(obj=resource)
    elif request.method == 'POST':
        form = forms.TaskForm()
        
    if form.validate_on_submit() and request.method == 'POST':
            form.populate_obj(resource)
            db.session.commit()
            return redirect("/task")
    
    if edit:
        button = "Update Resource"
    else: 
        button = ""
        
    return render_template('/task/new.html',
                       form=form,
                       url='/task/'+id+"?edit",
                       button=button)
  
@app.route('/task/new',methods=['GET','POST'])
def show_new_task():
    form = forms.TaskForm()
    if form.validate_on_submit():
        task = models.Task()
        form.populate_obj(task)
        db.session.add(task)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('task/new.html',
                               form=form,
                               button="Add New Task")
        


##########################################################
@app.route('/resource', methods=['GET'])
def resource():
    resources = models.Resource.query.all()
    return render_template('/resource/index.html',
                           title='Home',
                           resources=resources)

@app.route('/resource/<id>',methods=['GET','POST'])
def edit_resource(id):
    edit = request.args.get('edit') is not None
    resource = models.Resource.query.get(int(id))
    form = None
    
    if request.method == 'GET':
        form = forms.ResourceForm(obj=resource)
    elif request.method == 'POST':
        form = forms.ResourceForm()
        
    if form.validate_on_submit() and request.method == 'POST':
            form.populate_obj(resource)
            db.session.commit()
            return redirect("/resource")
    
    if edit:
        button = "Update Resource"
    else: 
        button = ""
        
    return render_template('/resource/new.html',
                       form=form,
                       url='/resource/'+id+"?edit",
                       button=button)
  
@app.route('/resource/new',methods=['GET','POST'])
def show_new_resource():
    form = forms.ResourceForm()
    if form.validate_on_submit():
        resource = models.Resource()
        form.populate_obj(resource)
        db.session.add(resource)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('resource/new.html',
                               form=form,
                               button="Add New Task")
        
####################################

@app.route('/timesheet', methods=['GET','POST'])
def timesheets():
    return render_template('/timesheet/index.html',
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
    