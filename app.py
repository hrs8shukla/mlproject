# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 02:44:10 2020

@author: Harsh Enterprises
"""

from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
app = Flask(__name__)

model=pickle.load(open('logistic_regression.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        Gender= request.form['Gender']
        Married=request.form['Married']
        Dependents=request.form['Dependents']
        Education=request.form['Education']
        Self_Employed=request.form['Self_Employed']
        ApplicantIncome=int(request.form['ApplicantIncome'])
        CoapplicantIncome=int(request.form['CoapplicantIncome'])
        LoanAmount=int(request.form['LoanAmount'])
        Loan_Amount_Term=int(request.form['Loan_Amount_Term'])
        Credit_History=int(request.form['Credit_History'])
        Property_Area=request.form['Property_Area']
        prediction=model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
        output=round(prediction[0])
        if output==1:
            return render_template('index.html',prediction_text="You are Eligible for Loan")
        elif output==0:
            return render_template('index.html',prediction_text="You are Not Eligible for Loan")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)