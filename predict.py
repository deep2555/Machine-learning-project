import json
import requests

# creating input fo user
bmi = input("enter BMI: " )
age = input("enter age: ")
gulcose = input("enter gulcose: ")
pregnancy = input("enter pregnancy: ")

# creating the request 
url = "http://127.0.0.1:5000/"
data = {"bmi": bmi, "age":age , "gulcose":gulcose, "pregnancy":pregnancy}
dataJSON = json.dumps(data)
headers = {"Content-type" :"application/json"}
response = requests.post(url = url, data = dataJSON, headers = headers)
print(response)
output =json.loads(response.text)

prediction = output["prediction"]
print("diabetic" if prediction ==1 else "not diabetic")