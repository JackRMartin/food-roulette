from urllib.request import urlopen
import json

# Get the dataset
base_url = 'http://api.ipstack.com/'
ip = 1
key = '?access_key=98a13c3077a3992fd956e2a6f1b8dd43'
url = 'http://api.ipstack.com/137.151.174.24?access_key=98a13c3077a3992fd956e2a6f1b8dd43'
response = urlopen(url)

# Convert bytes to string type and string type to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)

print(json_obj['city']) # prints the string with 'source_name' key
