import json

userInfo = {"Name": "Chris", "Age": "29", "Occupation": "Doctor", "Contact": "745-093-8769"}

with open('exampleWrite.json','r+') as f:
    json.dump(userInfo,f)