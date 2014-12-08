from app import db
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey, PrimaryKeyConstraint

class Resources(db.Model):
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
    password = db.Column(db.String(120))
    
class Projects(db.Model):
    #Create Table Projects
    projectName = db.Column(db.String(120), primary_key = True, unique=True)
    projectStartDate = db.Column(db.date)
    projectEndDate = db.Column(db.date)
    manager = db.Column(Integer, ForeignKey(Resources.id))
    
class Tasks(db.Model):
    #Create Table Tasks
    taskName = db.column(String(120), primary_key=True)
    projectName = db.column(String(120), primary_key = True, ForeignKey(Projects.projectName))
    startDate= db.column(Date)
    endDate = db.column(Date)
    empID = db.column(Integer, ForeignKey(Resources.id))
                            
class Timesheets(db.Model):
    #Create Table Timesheets
    weekStart = db.Column(db.date, primary_key=True, unique=True)
    empID = column(Integer, ForeignKey(Resources.id))
    projName = column(String(120), ForeignKey(Projects.projectName))
    taskName = column(String(120), ForeignKey(Tasks.taskName), unique = True)
    hoursWorked = column(Integer)
    
    
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
        

    def __repr__(self):
        return '<Resources %r>' % (self.lastName)