from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(99), index=True)
    picture = Column(String)
    email = Column(String)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(99), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    description = Column(String(999))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
        }


class Wine(Base):
    __tablename__ = 'wine'

    name =Column(String(99), nullable = False)
    id = Column(Integer, primary_key = True)
    origin = Column(String(999))
    description = Column(String(999))
    price = Column(String(8))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'origin': self.origin,
            'id': self.id,
            'price': self.price,
        }

engine = create_engine('sqlite:///winelistwithusers.db')
 
Base.metadata.create_all(engine)