from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Measure(db.Model):

    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(240), unique=False, nullable=True)
    date = db.Column(db.String(120), unique=False, nullable=True)
    temperature = db.Column(db.String(120),unique=False, nullable=True)
    hour = db.Column(db.String(120),unique=False, nullable=True)


    def __repr__(self):
        return '<Data %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "position": self.position,
            "date": self.date,
            "temperature": self.temperature,
            "hour": self.hour
        }