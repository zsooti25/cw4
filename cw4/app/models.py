from app import db


class City(db.Model):
    __table__ = db.Model.metadata.tables['city']


class Forecast(db.Model):
    __table__ = db.Model.metadata.tables['forecast']


class User(db.Model):
    __table__ = db.Model.metadata.tables['user']
