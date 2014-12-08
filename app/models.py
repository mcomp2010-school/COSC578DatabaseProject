from app import db
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from werkzeug import generate_password_hash
from werkzeug import check_password_hash

class Resource(db.Model):
    #CREATE TABLE ROCUE
    __tablename__ = 'resources'
    #Create Table Resources
    id = db.Column(db.Integer, primary_key=True, unique=True)
    firstName = db.Column(db.String(64), index=True)
    lastName = db.Column(db.String(120), index=True)
    phoneNumber = db.Column(db.String(120))
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    zip = db.Column(db.String(10))
    position = db.Column(db.String(120))
    team = db.Column(db.String(120))
    role = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    
    def __init__(self, name=None, email=None):
        self.firstName = name
        self.email = email
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
        
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
                               
    def __repr__(self):
        return '<Resource %r>' % (self.email)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    projectName = db.Column(db.String(120), unique=True)
    projectStartDate = db.Column(db.Date)
    projectEndDate = db.Column(db.Date)
    manager = db.Column(db.Integer, ForeignKey(Resource.id))
    
class Task(db.Model):
    #Create Table Tasks
    taskName = db.Column(db.String(120), primary_key=True)
    projectName = db.Column(db.String(120), primary_key = True)
    startDate= db.Column(db.Date)
    endDate = db.Column(db.Date)
    empID = db.Column(db.Integer, ForeignKey(Resource.id))
    
class Timesheet(db.Model):
    #Create Table Timesheets
    weekStart = db.Column(db.Date, primary_key=True, unique=True)
    empID = column(db.Integer, ForeignKey(Resource.id))
    projName = column(db.String(120), ForeignKey(Project.projectName))
    taskName = column(db.String(120), ForeignKey(Task.taskName))
    hoursWorked = column(db.Integer)
