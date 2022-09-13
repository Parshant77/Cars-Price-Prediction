

from flask import *
import pickle
import sklearn

app=Flask(__name__)


def make_pred(inps):
    model = pickle.load(open('C:\\Itvedant\\Machin Learning\\project\\price_pred.pkl','rb'))
    res=model.predict([inps])[0]
    return res


@app.route("/")
def home_fun():

    return render_template("main_form.html")

@app.route("/pred_link",methods=["POST"])
def check_fun():
    make_in=int(request.form["make_in"])    
    fuel_in=int(request.form["fuel_in"])
    body_in=int(request.form["body_in"])
    wheel_in=int(request.form["wheel_in"])
    engine_in=int(request.form["engine_in"])
    enginetype_in=int(request.form["enginetype_in"])
    symbol_in=int(request.form["symbol_in"])
    normalized_in=int(request.form["normalized_in"])
    width_in=int(request.form["width_in"])
    height_in=int(request.form["height_in"])
    enginesize_in=int(request.form["enginesize_in"])
    horsepower_in=int(request.form["horsepower_in"])
    citympg_in=int(request.form["citympg_in"])
    highwaympg_in=int(request.form["highwaympg_in"])

    ip_params=[make_in,fuel_in,body_in,wheel_in,engine_in,enginetype_in,symbol_in,normalized_in,width_in,
    height_in,enginesize_in,horsepower_in,citympg_in,highwaympg_in]

    result=make_pred(ip_params)
    return render_template("display_res.html",res=result)




if __name__=="__main__":
    app.run(debug=True)

