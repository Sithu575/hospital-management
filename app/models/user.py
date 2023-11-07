from app.extensions import db
from datetime import datetime
from sqlalchemy.orm import relationship

class User(db.Model):
    user_id=db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    dob = db.Column(db.String(20))
    age = db.Column(db.Integer, index=True)
    gender=db.Column(db.String(64))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    add_phone=db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)
    adhaar=db.Column(db.String(120), index=True)
    created_date = db.Column(db.DateTime, default=datetime.now)
    created_by=db.Column(db.String(64))
    updated_date = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)
    updated_by=db.Column(db.String(20))

   
    credential = db.relationship('Credential', backref='user')


    def __repr__(self):
        return f'<user {self.user_id}>'
   