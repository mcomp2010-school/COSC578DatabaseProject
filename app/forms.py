from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    last_name = StringField('LastName', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)