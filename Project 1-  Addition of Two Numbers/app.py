from flask import Flask, request, render_template
import numpy as np
import pickle
#Create Flask app
app = Flask(__name__)

#Load the pickle Model
model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=["POST"])
def predict():
    float_number =[float (x) for x in request.form.values()]
    feature = [np.array(float_number)]
    result = model.predict(feature)
    return render_template('index.html',prediction_text= f"Sum of two numbers bu Machine Learning is {result}")


if __name__ == '__main__':
    app.run(debug=True)