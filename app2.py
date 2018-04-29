#Importing dependencies

from flask import Flask,render_template, jsonify, request
import pickle
loaded_model = pickle.load(open('RandomForest_model.sav', 'rb'))
# result = loaded_model.score(X_test, y_test)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index2.html' )

@app.route('/', methods=['POST'])
def predict(prediction=None):
    age = request.form['Age']
    gender = request.form['Gender']
    education = request.form['education']
    marriage = request.form['marriage']
    credit_score = request.form['credit_score']
    creditA = request.form['Credit']
    credit_bill = request.form['Credit Bill']
    bill_payment = request.form['Bill Payment']


    #These are the features that need to be past in the model from our dataset
    # prediction = loaded_model.predict([[ LIMIT_BAL_US, SEX , EDUCATION , MARRIAGE, AGE, PAY_SCORE_AVG, BILL_AVG_US, PAY_AMT_AVG_US
    #                                      PAY_TO_BILL, CREDIT_UTILIZATION]])

    #this is the format how the values in model.predict should look like
    # prediction = loaded_model.predict([[ 2.17714286e+03, 2.00000000e+00, 2.00000000e+00, 2.00000000e+00, 2.20000000e+01,
    #                                      2.17000000e+00, 1.70386829e+03, 4.67360000e+01, 3.00000000e-02, 1.02596667e+00]])


    new_age = int(age)
    new_sex = int(gender)
    new_education = int(education)
    new_marriage = int(marriage)
    prediction = loaded_model.predict([[ creditA, new_sex , new_education , new_marriage, new_age,
                                         2.17000000e+00, credit_bill, bill_payment, 7.30000000e-01, 5.69950000e-02]])
    # if prediction[0] == 1:
    #     new_prediction = "Default !"
    # else:
    #     new_prediction = "Non-default"

    #

    return render_template('index2.html', prediction=prediction )



if __name__ == '__main__':
	app.run(debug=True)
