from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, insert, delete
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Relationships(db.Model):
    __tablename__ = 'relationships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Relationships %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    lastName = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastName": self.lastName,
            "age": self.age,
        }
    
class Relative(db.Model):
    __tablename__ = 'relative'
    id = db.Column(db.Integer, primary_key=True)
    personID = db.Column(db.Integer, ForeignKey('person.id'), unique=False, nullable=False)
    relativeID = db.Column(db.Integer, ForeignKey('person.id'), unique=False, nullable=False)
    relationshipID = db.Column(db.Integer, ForeignKey('relationships.id'), unique=False, nullable=False)
    Person = relationship("Person", foreign_keys=[personID])
    Relative = relationship("Person", foreign_keys=[relativeID])
    Relationships = relationship(Relationships)

    def __repr__(self):
        return '<Parents %r>' % self.personID

    def serialize(self):
        return {
            "id": self.id,
            "personID": self.personID,
            "relativeID": self.relativeID,
            "relationship": self.relationshipID,
        }

#class Children(db.Model):
#    __tablename__ = 'children'
#    id = db.Column(db.Integer, primary_key=True)
#    personID = db.Column(db.Integer, ForeignKey('person.id'), unique=False, nullable=False)
#    childID = db.Column(db.Integer, ForeignKey('person.id'), unique=False, nullable=False)
#    relationshipID = db.Column(db.Integer, ForeignKey('relationships.id'), unique=False, nullable=False)
#    Person = relationship("Person", foreign_keys=[personID])
#    Child = relationship("Person", foreign_keys=[childID])
#    Relationships = relationship(Relationships)

#    def __repr__(self):
#        return '<Children %r>' % self.personID

#    def serialize(self):
#        return {
#            "id": self.id,
#            "personID": self.personID,
#            "childID": self.childID,
#            "relationship": self.relationshipID,
#        }