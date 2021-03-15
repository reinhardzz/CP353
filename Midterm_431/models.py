from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"

    name = db.Column(db.String, primary_key=True)
    energy = db.Column(db.Integer())
    protein = db.Column(db.Integer())
    fat = db.Column(db.Integer())
    carbohydrate = db.Column(db.Integer())
    

    def __repr__(self):
        return f"{self.name}:{self.energy}:{self.protein}:{self.fat}:{self.carbohydrate}"