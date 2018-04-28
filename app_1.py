#Importing dependencies

import numpy as np
import pandas as pd

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///creditcarddefault.sqlite', echo=True)


#Initializing app
app=Flask(__name__)

#Creating database
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///creditcarddefault.sqlite"
# db = SQLAlchemy(app)


# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()


# #Creating session

Base = declarative_base()

class CreditDefault(Base):
	__tablename__ = "credit_default"

	id = Column(Integer,primary_key="True")
	age = Column(Integer)
	gender = Column(Integer)
	education = Column(Integer)
	marriage = Column(Integer)
	credit = Column(Integer)
	credit_bill = Column(Integer)
	bill_payment = Column(Integer)
	billing_hist=Column(Integer)


engine = create_engine('sqlite:///creditcarddefault.sqlite', echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.drop_all() 
Base.metadata.create_all(engine) 



@app.route("/")
def home():
	return render_template("index.html")

@app.route("/submit",methods=["GET","POST"])
def submit():
	if request.method=="POST":
		newCreditObj = CreditDefault(
			gender = request.form["gender"],
			education = request.form["education"],
			marriage = request.form["marriage"],
			age =  request.form["age"],
			credit = request.form["credit"],
			credit_bill = request.form["credit_bill"],
			bill_payment = request.form["bill_payment"],
			billing_hist = request.form["credit_score"])
		session.add(newCreditObj)
		session.commit()
		return redirect('http://localhost:5000/',code=302)
		# flash('New Credit obj created')

		# 	if billing_hist == "I do not carry a balance"
		# 		billing_hist = -2
		# 	elif billing_hist == "Always On Time"
		# 		billing_hist = -1
		# 	elif billing_hist == "30+ day past due"
		# 		billing_hist = 0
		# 	elif billing_hist == "60+ day past due"
		# 		billing_hist = 1
		# 	elif billing_hist == "90+ day past due"
		# 		billing_hist = 2
		# 	else billing_hist == "120+ day past due"
		# 		billing_hist = 3

		# credit = creditDefault(age=age,gender=sex,education=education,marriage=marriage,credit_avail=credit_avail,last_mo_credit_bill=last_mo_credit_bill,last_mo_credit_payment=last_mo_credit_payment)
		# session.add(credit)
		# session.commit()
		# flash("thanks for your entry")
	return render_template("index_form.html")

@app.route("/api/query")
def query():




	

	# for result in results:
	# 	print(result.gender)
	# 	print(result.education)

# pet_type = [result[0] for result in results]
# age = [result[1] for result in results]

# pet_data = {
#     "x": pet_type,
#     "y": age,
#     "type": "bar"
# }



# 		#after they hit submit, i want a flash() to happen? and then to return the classfication
# 		#on the screen. 

if __name__ == "__main__":
	app.run(debug=True)




