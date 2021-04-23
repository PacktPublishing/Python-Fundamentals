import json

# Imagine we are trying to fill in some information on web forms online #
# All the intered information will be saved as a json #
userInfo = {"Name": "Chris", "Age": "29", "Occupation": "Doctor", "Contact": "745-093-8769"}

# Create Json object
EncodejsonObj = json.dumps(userInfo)

with open('example.json','r+') as f:
    json.dump(userInfo,f)

print(EncodejsonObj)
print(type(EncodejsonObj))
# Send the json file to the server #


# Receive and decode json file
# Read a Json object
DecodejsonObj = json.loads(EncodejsonObj)
print(DecodejsonObj)
print(type(DecodejsonObj))

print(userInfo['monkeys'])