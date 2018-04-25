#Importing dependencies

import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import (Flask,jsonify,render_template,jsonify,request,redirect)

##IMPORTING MODELS

#Initializing app
app=Flask(__name__)

#Creating database
from flask_sqlalchemy import SQLAlchemy 
engine = create_engine('sqlite:///creditcarddefault.sqlite', echo=True)
Base = declarative_base()
db=SQLAlchemy(app)


#Creating session
session=engine(Session)

class creditDefault(Base):
	__tablename__ = 'credit_default'

	id = db.Column(db.Integer,primary_key='True')
	limit_bal = db.Column(db.Integer)
	sex = db.Column(db.Integer)
	education = db.Column(db.Integer)
	marriage = db.Column(db.Integer)
	age = db.Column(db.Integer)
	



