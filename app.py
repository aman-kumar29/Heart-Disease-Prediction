from flask import Flask,render_template,request 
import pickle  
import pandas as pd

app=Flask(__name__)
model = pickle.load(open('Heartdisease82.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   age = request.form.get('age')
   maxhr = request.form.get('maxhr')
   chloresterol = request.form.get('chol')
   sex = request.form.get('sex')
   bp = request.form.get('bp')
   stde = request.form.get('stde')
   chestpain = request.form.get('chest')
   fbs = request.form.get('fbs')
   ekg = request.form.get('ekg')
   exercise = request.form.get('exercise')
   slope = request.form.get('slopest')
   caa = request.form.get('caa')
   thallium = request.form.get('thallium')
   li=[age,sex,chestpain,bp,chloresterol,fbs,ekg,maxhr,exercise,stde,slope,caa,thallium] 
   result = model.predict([li])[0]
   if(result==1):
        return render_template('index.html', label =1)
   else:
        return render_template('index.html', label =-1)

    

if __name__ == '__main__':
    app.run(debug=True)
