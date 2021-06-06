# importing libraries
import pickle
import numpy as np
from flask import Flask, request,json,jsonify
import requests

# global variables
app= Flask(__name__)
loaded_model = pickle.load(open("diabetes.sav", "rb"))

# used defined

@app.route("/", methods = ["POST"])
def predict():
    user_input = request.json
    print(user_input)
    input_list = [user_input["gulcose"], user_input["bmi"], user_input["pregnancy"], user_input["age"]]
    # print(loaded_model.predict([100,30,45,25]))
    # pass
    prediction = loaded_model.predict([input_list])
    confidence = loaded_model.predict_proba([input_list])
    response = {}
    response["prediction"] = int(prediction[0])
    response["confidence"] = str(round(np.amax(confidence[0]) *100,2))
    return jsonify(response)
    # print(prediction)
    # print(confidence)

# main function
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)