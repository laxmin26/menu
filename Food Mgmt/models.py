from app import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    is_veg = db.Column(db.Boolean, default=True)
    nutritional_value = db.Column(db.String(100))
