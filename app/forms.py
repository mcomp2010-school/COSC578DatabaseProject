from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import DateField
from wtforms import IntegerField
from wtforms.ext.appengine.db import model_form
from wtforms import BooleanField
from wtforms.validators import DataRequired
from wtforms import validators
from app import models

class LoginForm(Form):
    last_name = StringField('LastName', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    
class ResourceForm(Form):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip = StringField('Zip', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    team = StringField('Team', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    password = StringField('Password')

class ProjectForm(Form):
    projectName = StringField('Project Name', validators=[DataRequired()])
    projectStartDate = DateField('Project Start Date',  format='%m/%d/%Y')
    projectEndDate = DateField('Project End Date',  format='%m/%d/%Y')
    manager = IntegerField('Manager', validators=[DataRequired()])

class TaskForm(Form):
    pass