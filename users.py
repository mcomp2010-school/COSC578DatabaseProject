from app import db, models

u = models.Resources(lastName='john')

db.session.add(u)
db.session.commit()