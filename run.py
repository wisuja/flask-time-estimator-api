from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
  model = pickle.load(open('finalized_model.sav', 'rb'))
  scaler = pickle.load(open('scaler.sav', 'rb'))

  task_type = request.form.get('task_type')
  number_of_peoples = request.form.get('number_of_peoples')

  originalRequest = {
    'task_type': [task_type],
    'number_of_peoples': [number_of_peoples],
    'estimated_time_in_minutes': [0]
  }

  df = pd.DataFrame.from_dict(originalRequest)
  df[list(df.columns)] = scaler.transform(df)
  df = df.drop(columns='estimated_time_in_minutes')

  prediction = model.predict(df).tolist()
  df['estimated_time_in_minutes'] = prediction

  scaledPrediction = scaler.inverse_transform(df)
  finalPrediction = scaledPrediction[0, 2]

  response = {
    'prediction': finalPrediction
  }

  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True)
