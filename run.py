from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
  model = pickle.load(open('finalized_model.sav', 'rb'))

  task_type = request.form.get('task_type')
  number_of_peoples = request.form.get('number_of_peoples')

  df = pd.DataFrame({
    'task_type': [task_type],
    'number_of_peoples': [number_of_peoples]
  })

  prediction = model.predict(df).tolist()
  response = {
    'prediction': prediction
  }

  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True)
