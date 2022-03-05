#!/usr/bin/env python
# coding: utf-8

# In[31]:


from flask import Flask


# In[32]:


app = Flask(__name__)


# In[33]:


from flask import request, render_template
import joblib 

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        age = request.form.get("age")
        income = request.form.get("income")
        loan = request.form.get("loan")
        age = float(age)
        income = float(income)
        loan = float(loan)
        print(age, loan, income)
        model1 = joblib.load("EquityDT")
        pred1 = model1.predict([[age,income,loan]])
        if pred1[0] == 0:
            decision = "No"
        else: 
            decision = "Yes"
        s1 = "Predicted loan default on Decision Tree is " + decision
        model2 = joblib.load("EquityREG")
        pred2 = model2.predict([[age,income,loan]])
        if pred2[0] == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s2 = "Predicted loan default on Linear Regression is " + decision
        model3 = joblib.load("EquityNN")
        pred3 = model3.predict([[age,income,loan]])
        if pred3[0] == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s3 = "Predicted loan default on Neural Network is " + decision
        model4 = joblib.load("EquityRF")
        pred4 = model4.predict([[age,income,loan]])
        if pred4[0] == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s4 = "Predicted loan default on Random Forest is " + decision
        model5 = joblib.load("EquityGB")
        pred5 = model5.predict([[age,income,loan]])
        if pred5[0] == 0:
            decision = "No"
        else: 
                decision = "Yes"
        s5 = "Predicted loan default on Gradient Boosting is " + decision
        return(render_template("index.html",result1=s1,result2=s2,result3=s3,result4=s4,result5=s5))
    else: 
        return(render_template("index.html",result1="2",result2="2",result3="2",result4="2",result5="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()

