# coding: utf-8

"""
    base.models
    ~~~~~~~~~~~

    The most common models for the whole project.

    :copyright: (c) 2015 by Roman Zaiev.
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ext import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_


class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        if any(
            (isinstance(id, basestring) and id.isdigit(),
             isinstance(id, (int, float))),
        ):
            return cls.query.get(int(id))
        return None

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()
        
class Event(UserMixin, CRUDMixin, db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(600))
    notification = db.Column(db.String(600))
    promote = db.Column(db.Boolean)
    photo = db.Column(db.String(100))
    
    def __init__(self, promote_, title_, description_, notify_, photo_):		
        self.title = title_
        self.description = description_
        self.notification = notify_
        self.promote = promote_
        self.photo = photo_
    
    @classmethod
    def get_by_id(cls, id):
        return Event.query.filter(Event.id == id).first()
            
    @classmethod
    def get_promotes(cls, limit_):
        return Event.query.filter(and_(Event.promote.contains(1))).limit(limit_)

    def __repr__(self):
		return u"<Event ('{0}','{1}','{2}','{3}','{4}') >".format(self.id, self.title , self.description, self.promote, self.photo)


class Schedule(UserMixin, CRUDMixin, db.Model):
    __tablename__ = 'schedules'

    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Integer)
    title = db.Column(db.String(200))    
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    opened = db.Column(db.Boolean)

    def __init__(self, event_, title_, start_, end_):
        self.event = event_
        self.title = title_
        self.start = start_
        self.end = end_
        self.opened = True # default value

    @classmethod
    def get_by_id(cls, id):
        return Schedule.query.filter(Schedule.id == id).first()
        
    @classmethod
    def get_openning(cls):
        return Schedule.query.filter(and_(Schedule.opened.contains(1)))

    def __repr__(self):
        return u'<Schedule %r>' % self.name

class User(UserMixin, CRUDMixin, db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return u'<User %r>' % self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
