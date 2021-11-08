from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
  prediction = 1
  response = {
    'prediction': prediction
  }

  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True)
