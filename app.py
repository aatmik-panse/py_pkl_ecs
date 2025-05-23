from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello from Flask"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    Gender = int(data['Gender'])
    Married = int(data['Married'])
    Credit_History = int(data['Credit_History'])
    Total_Income_Log = float(data['Total_Income_Log'])

    input_features = np.array([[Gender, Married, Credit_History, Total_Income_Log]])
    prediction = model.predict(input_features)[0]
    result = "Loan Approved" if prediction == 1 else "Loan Rejected"

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)