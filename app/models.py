rom . import db

class Property(db.Model):

    __tablename__ = 'property'

    propertyID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(255))
    rooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    price = db.Column(db.String(20))
    property = db.Column(db.String(20))
    location = db.Column(db.String(150))
    filename = db.Column(db.String(255)) 

    def __init__(self, title, description, no_room, no_bath, price, type, location, filename):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.property = property
        self.location = location
        self.filename = filename
        
