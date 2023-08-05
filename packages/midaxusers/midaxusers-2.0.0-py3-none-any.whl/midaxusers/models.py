from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, String, Integer, DateTime, Column, Boolean, CHAR, Sequence, ForeignKey, Index
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func, expression
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.dialects.oracle import RAW
from sqlalchemy.types import PickleType
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.collections import attribute_mapped_collection
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import abort, jsonify
from sqlalchemy import types, and_, or_, TypeDecorator
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.ext.hybrid import hybrid_property
#from sqlalchemy.schema import Column
import uuid
import binascii
import json
from collections import namedtuple
import collections

db = SQLAlchemy()
migrate = Migrate()

class HybridUniqueIdentifier(TypeDecorator):
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mssql':
            return dialect.type_descriptor(UNIQUEIDENTIFIER)
        elif dialect.name == 'oracle':
            return dialect.type_descriptor(RAW(16))
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'mssql':
            if not isinstance(value, uuid.UUID):
                return str(uuid.UUID(value))
            else:
                return str(value)
        elif dialect.name == 'oracle':
            if not isinstance(value, uuid.UUID):
                return uuid.UUID(value).bytes
            else:
                return value.bytes
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'mssql':
            if not isinstance(value, uuid.UUID):                
                value = uuid.UUID(value)
            return value
        elif dialect.name == 'oracle':
            if not isinstance(value, uuid.UUID):                
                value = uuid.UUID(bytes = value)
            return value
        else:            
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value



def generate_uuid():
   return str(uuid.uuid4())    

class User(db.Model):
    __tablename__ = 'USERS'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    uuid = Column(HybridUniqueIdentifier(), default=uuid.uuid4)
    _domain = Column('domain', String(64), index=True)    
    role = Column(Integer)        
    active = Column(Boolean, server_default=expression.true())
    first_name = Column(String(64))
    middle_name = Column(String(64))
    last_name = Column(String(64))
    phone = Column(String(64))
    position = Column(String(20))
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())    
    logins = relationship('UserLogin', backref = 'user', collection_class=attribute_mapped_collection('login_type'),
                cascade="all, delete-orphan")
    attributes = relationship('UserAttributes', backref = 'user', collection_class=attribute_mapped_collection('name'),
                cascade="all, delete-orphan")

    __table_args__ = (       
        UniqueConstraint('uuid', name='user_uuid_uq'),
                     )

    @hybrid_property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value.casefold().strip('^ ')

    def __init__(self, named_tuple_user = None, **kwargs):
        super(User, self).__init__(**kwargs)

        if named_tuple_user is not None:
            gen = (x for x in dir(named_tuple_user) if not x.startswith('__'))

            for a in gen:
                if a not in dir(self):
                    pass
                elif a == 'logins': 
                    for key, value in getattr(named_tuple_user, a).items():                        
                        value['login_type'] = key                              
                        self.logins[key] = UserLogin(value)
                else:
                    setattr(self, a, getattr(named_tuple_user, a))
                    
                    
                                   


    def serialize(self):
        return {            
            'uuid': str(self.uuid),
            'active': str(self.active),
            'domain': self.domain,
            'role':str(self.role),
            'first_name':self.first_name,
            'middle_name':self.middle_name,
            'last_name':self.last_name,
            'phone':self.phone,
            'position':self.position,
            'logins': { key : value.serialize() for key, value in self.logins.items()},
            'user_attributes': {key : value.value for key, value in self.attributes.items()}
        }
    '''
    def logins_set(self, values):
        for value in values:
            if UserLogin.query.filter_by(user_uuid = self.uuid, login_type = value['login_type']).first() is None:
                newlogin = UserLogin()
                newlogin.login_key = value['login_key']               
                newlogin.password = value['password']
                if value['force_password_change'] is not None and value['force_password_change'] == 'True':
                    newlogin.force_password_change = True
                if newlogin.login_key is not None and len(newlogin.login_key) >= 1 and newlogin.password is not None and len(newlogin.password) >= 1:
                   db.session.add(newlogin)

            for e in UserLogin.query.filter_by(user_uuid = self.uuid, login_type = value['login_type']).all():
                if value['password'] is not None and len(value['password']) >= 1:
                    e.password = value['password']
                if value['login_key'] is not None and len(value['login_key']) >= 1:
                    e.login_key = value['login_key']
                if value['force_password_change'] is not None and value['force_password_change'] == 'True':
                    e.force_password_change = True
                if e.login_key is not None and len(e.login_key) >= 1 and e.password is not None and len(e.password) >= 1:
                    pass
                else:
                    db.session.delete(e)                        
        
                


    logins = property()
    logins = logins.setter(logins_set)    
    '''
    @classmethod
    def search(cls, searched_uuid, active = True):        
        if not isinstance(searched_uuid, uuid.UUID):
            searched_uuid = uuid.UUID(searched_uuid)

        user = cls.query.filter_by(uuid = searched_uuid).first()

        if user is None:
            raise NoResultFound("User Not Found")

        return user
   

    #def __repr__(self):
    #    return '<Domain {} User {}>'.format(self.domain, self.username)
    
    #def __str__(self):
    #      return '<{}@{}>'.format(self.username, self.domain)  

class PasswordNeedsResetError(Exception):
    def __init__(self, user, msg=None):
        if msg is None:            
            msg = 'Your Password Needs To Be Reset'
        super(PasswordNeedsResetError, self).__init__(msg)
        self.user = user

class UserLogin(db.Model):
    __tablename__ = 'USER_LOGINS'
    id = Column(Integer, Sequence('users_logins_seq'), primary_key=True)
    user_uuid = Column(HybridUniqueIdentifier(), ForeignKey('USERS.uuid'), index = True, nullable = False)
    login_type = Column(String(40), nullable = False)
    login_key = Column(String(120), nullable = False)
    password_hash = Column(String(256), nullable = False)
    force_password_change = Column(Boolean, server_default=expression.false())
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    __table_args__ = (        
        UniqueConstraint('login_type', 'login_key', name='login_user_uq'),
                     )

    def password_set(self, value):
        self.password_hash = generate_password_hash(value, method='pbkdf2:sha512', salt_length=16)               

    password = property()
    password = password.setter(password_set)  

    def __init__(self, *initial_data, **kwargs):
        super(UserLogin, self).__init__(**kwargs)

        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])

    def serialize(self):
        return {
            'login_key' : self.login_key,
            'force_password_change' : str(self.force_password_change)
        }
        
              

    def check_password(self, value):        
        if self.password_hash is not None and value is not None:
            return check_password_hash(self.password_hash, value)
        return False

    @staticmethod
    def get_user(credentials, check_password = False):
        login = UserLogin.query.filter_by(login_type = credentials['login_type'], login_key = credentials['login_key']).first()

        if login is None:
            raise NoResultFound("No Login Found")

        if check_password is True:
            if login.check_password(credentials['password']) is False:
                raise ValueError("Wrong password")   

            if login.force_password_change is True:
                raise PasswordNeedsResetError(login.user)     

        user = login.user

        if user is None:
            raise NoResultFound("No User Found")

        return user

class UserAttributes(db.Model):
    __tablename__ = 'USER_ATTRIBUTES'

    user_uuid = Column(HybridUniqueIdentifier(), ForeignKey('USERS.uuid'), index = True, nullable = False)
    name = Column(String(64))
    value = Column(String(64))
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    __table_args__ = (PrimaryKeyConstraint('user_uuid', 'name', name='userattributes_pk'),
                     )
    
                
    def __repr__(self):
        return '<{}:{}>'.format(self.name, self.value)  



