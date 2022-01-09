import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/predict/', methods=['GET', "POST"])
def predict():
  input_values = [float(x) for x in request.form.values()]
  inp_features = [input_values]
  prediction = model.predict(inp_features)
  if prediction==1:
    return render_template('index.html', Hasil_Prediksi='Kriteria keluhan diatas menyebabkan kematian')
  else:
    return render_template('index.html', Hasil_Prediksi='Kriteria keluhan diatas tidak menyebabkan kematian')

app.run(debug = True)