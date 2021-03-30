from flask import Flask, jsonify,  request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model_load = joblib.load("./models/Model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if (request.method == 'POST'):
        int_features = [x for x in request.form.values()]
        final_features = [np.array(int_features)]
        output = model_load.predict(final_features).tolist()
        res = ''
        if(output == [1.0]):
            res = 'The customer will soon leave (Churn) the telecom network.'
        else:
            res = 'Happy Customer'
            
        return render_template('index.html', prediction_text=res)
    else :
        return render_template('index.html')

@app.route("/predict_api", methods=['POST', 'GET'])
def predict_api():
    print(" request.method :",request.method)
    if (request.method == 'POST'):
        data = request.get_json()
        return jsonify(model_load.predict([np.array(list(data.values()))]).tolist())
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)