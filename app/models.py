from app import db

class Resources(db.Model):
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