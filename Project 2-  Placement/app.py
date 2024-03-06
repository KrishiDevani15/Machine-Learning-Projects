from flask import Flask, render_template, request, jsonify, redirect, url_for
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
print("hello world")

# Load the HTML form for data entry
@app.route('/')
def index():
    return render_template('index.html')

# Receive and process the form submission
@app.route('/submit_data', methods=['POST'])
def submit_data():
    # Get form data
    age = int(request.form['age'])
    stream = request.form['stream']
    internships = int(request.form['internships'])
    cgpa = float(request.form['cgpa'])
    hostel = request.form['hostel']
    backlogs = int(request.form['backlogs'])

    # Convert stream to numeric value
    stream_values = {
        "Electronics and Communication": 0,
        "Computer Science": 1,
        "Mechanical": 2,
        "Civil": 3,
        "Information Technology": 4,
        "Electrical": 5
    }

    numeric_stream = stream_values.get(stream)

    # Encode hostel (Yes/No) to 1/0
    hostel_encoded = 1 if hostel.lower() == 'yes' else 0

    # Prepare the data for prediction
    input_data = [[age, numeric_stream, internships, cgpa, hostel_encoded, backlogs]]

    # Load the trained model
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Make a prediction
    prediction = model.predict(input_data)[0]

    # Save input data and prediction to display on the prediction page
    data = {
        'age': age,
        'stream': stream,
        'internships': internships,
        'cgpa': cgpa,
        'hostel': hostel,
        'backlogs': backlogs,
        'prediction': 'Placed' if prediction == 1 else 'Not Placed'
    }

    with open('prediction.pkl', 'wb') as file:
        pickle.dump(data, file)

    # Redirect to the prediction page
    return redirect(url_for('prediction'))

# Prediction page to display the saved prediction
@app.route('/prediction')
def prediction():
    # Load prediction data from prediction.pkl
    with open('prediction.pkl', 'rb') as file:
        data = pickle.load(file)
    
    return render_template('prediction.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)