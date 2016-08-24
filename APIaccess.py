import requests

#Host: data.usajobs.gov
#User-Agent: andrew@beta.build
#Authorization-Key: 

url = 'https://data.usajobs.gov/api/search?Keyword=Software'
user = 'andrew@beta.build'
key = 
keyword = {'Keyword' : 'Ranger'}

r = requests.get(url, auth=(user, key))

print r.status_code
print r.raise_for_status()
print r.url
print r.content



