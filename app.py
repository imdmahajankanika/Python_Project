import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__,template_folder='templates')
model = joblib.load(open('ML_model.sav', 'rb'))
scaler = joblib.load("scaler.sav")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        features = [x for x in request.form.values()]
        Holiday=request.form.get('holiday')
        Seasons=request.form.get('season')
        Functioning=request.form.get('functioningDay')
        # Encoding the categorical features
        if(Holiday.lower=="no holiday"):
            features[9]=str(0)
        else:
            features[9]=str(1)
        
        if(Seasons=="Winter"):
            features[8]=str(3)
        elif(Seasons=="Summer"):
            features[8]=str(2)
        elif(Seasons=="Spring"):
            features[8]=str(1)
        elif(Seasons=="Autumn"):
            features[8]=str(0)

        if(Functioning.lower=="no"):
            features[10]=str(0)
        else:
            features[10]=str(1)
        
        final_features = [np.array(features)]
        # Scaling the final features
        final_features=scaler.transform(final_features)
        # Predicting the response
        prediction = model.predict(final_features)
        output = int(round(prediction[0]))
    return render_template('Result.html', prediction_text='Rented Bike Count:-  {}'.format(output))


@app.route('/results',methods=['POST'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    try:
        app.run(port=5000,debug=True)
    except:
        print("Oops! Server got exited unexpectedly.\nPlease contact server admin!")


