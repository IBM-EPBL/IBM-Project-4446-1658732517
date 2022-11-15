import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "Zc5JTfaTbgCdptIgwL8Q6_14NmQTQphyS0abzBjwSB4k"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["cylinders","displacement","horsepower","weight","acceleration","model year","origin"]], "values": [[8,307.0,130,3550,12.0,80,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3e8e56d6-a73f-4f4c-85f6-e3b5f4e51148/predictions?version=2022-11-13', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json()["predictions"][0]["values"][0][0])