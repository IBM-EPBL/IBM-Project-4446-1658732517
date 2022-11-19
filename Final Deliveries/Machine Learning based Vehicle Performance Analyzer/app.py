from flask import *
import pickle
app = Flask( __name__ ,template_folder='templates')
model = pickle. load (open( './regression.pkl' , 'rb'))
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
    p=model.predict(total)
    p=p[0]
    return render_template("result.html",label=str(p))


if __name__=='__main__':
    app.run()

