import pickle 
from flask import Flask , request

app = Flask(__name__)

@app.route('/' , methods=['GET',"POST"])
def index():
    if request.method == 'GET':
        return "Got a get request"
    filePath = open("iris.pkl" , "rb") 
    model = pickle.load(filePath)
    sl = request.form['sepal_length'] 
    sw = request.form['sepal_width']
    pl = request.form['petal_length'] 
    pw = request.form['petal_width']
    input = [sl, sw , pl , pw ]
    predictions = model.predict([input])
    return f"{predictions[0]}"