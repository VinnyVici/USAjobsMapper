import requests

#Host: data.usajobs.gov
#User-Agent: andrew@beta.build
#Authorization-Key: 

url = 'https://data.usajobs.gov'
user = 'andrew@beta.build'
key = 

r = requests.get(url, auth=(user, key))

print r.status_code

