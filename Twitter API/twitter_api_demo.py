from twitter_Credentials import key_secret
import base64 
import requests

# code adapted from: http://benalexkeen.com/interacting-with-the-twitter-api-using-python/

# first task: obtain a bearer token

base64_key_secret = base64.b64encode(key_secret) #encode to base64
finalized_key_secret = base64_key_secret.decode('ascii') #decode to ascii

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token/'.format(base_url)

auth_headers = {
	'Authorization':'Basic {}'.format(finalized_key_secret),
	'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
	'grant_type':'client_credentials'
}

r = requests.post(auth_url, headers=auth_headers, data= auth_data)

bearer_token = r.json()

print(bearer_token)
print(r.status_code)