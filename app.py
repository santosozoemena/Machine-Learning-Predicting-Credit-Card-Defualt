#importing dependencies

import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import (Flask,jsonify,render_template,jsonify,request,redirect)

##IMPORTING MODELS

#initializing app
app=Flask(__name__)

#Creating database
from flask_sqlalchemy import SQLAlchemy 
engine = create_engine('sqlite:///creditcarddefault.sqlite', echo=True)
Base = declarative_base()

