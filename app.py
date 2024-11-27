from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        previous_close = float(request.form['previous_close'])
        prediction = model.predict(np.array([[previous_close]]))
        predicted_price = round(prediction[0], 2)
        
        return render_template('prediction.html', prediction=predicted_price)
    except Exception as e:
        return render_template('error.html', error=str(e))



if __name__ == '__main__':
    app.run(debug=True)
