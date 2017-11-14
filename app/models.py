#app/models.py

from app import db



class Cocktail(db.Model):
    __tablename__  = 'Cocaktails'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ingredients = db.Column(db.String(1000))

    def __init__(self,name):
        self.name = name
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getall():
        return Cocktail.getall()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Cocktails: {}>".format(self.name)


class Bucketlist(db.Model):
    """This class represents a Bucketlist table"""

    __tablename__ = 'bucketlist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    def __init__(self, name):
        """Initialize with name """
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Bucketlist {}>".format(self.name)