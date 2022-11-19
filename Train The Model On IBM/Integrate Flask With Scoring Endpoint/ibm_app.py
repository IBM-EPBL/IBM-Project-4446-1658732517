from flask import *
import pickle
import requests
API_KEY = "tI0xOfFwTPctXvTyHPEA73tw6o5J4vv3xVsxoHFoPcx2"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
app = Flask( __name__ ,template_folder='templates')
#model = pickle. load (open(r"C:\Users\Kamalesh K\Desktop\IBM Project\IBM\Model Training\regression.pkl" , 'rb'))
@app. route ( '/' )
def intro() :
    return render_template("index.html")
@app. route ( '/app' )
def intro1() :
    return render_template("web.html")
@app.route('/predict',methods=["POST"])
def predict():
    a=request.form["a"]
    b=request.form["b"]
    c=request.form["c"]
    d=request.form["d"]
    e=request.form["e"]
    f=request.form["f"]
    g=request.form["g"]
    total=[[int(b),int(c),int(d),int(e),int(f),int(g),int(a)]]
    payload_scoring={"input_data":[{"field":[['f0','f1','f2','f3','f4','f5','f6']],"values":total}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/479bb755-b911-473c-9da4-a6d175e92ba0/predictions?version=2022-11-15', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    predictions=response_scoring.json()
    p=predictions['predictions'][0]['values'][0][0]
    #p=model.predict(total)
    #p=p[0]
    return render_template("result.html",label=str(p))


if __name__=='__main__':
    app.run()

