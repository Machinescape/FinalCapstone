from model import prediction
from flask import Flask, jsonify

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False  #Added the line because of solution found from https://stackoverflow.com/questions/60992849/attributeerror-request-object-has-no-attribute-is-xhr

@app.route('/predict', methods=['GET'])
def predict():
    predicted_talks = prediction()
    return jsonify(predicted_talks), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
