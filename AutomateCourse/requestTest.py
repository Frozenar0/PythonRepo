import requests
import os
os.environ['HTTP_PROXY'] = 'http://webproxy.bfm.com:8080'
os.environ['HTTPS_PROXY'] = 'https://webproxy.bfm.com:8080'

xyz = requests.get('http://api.github.com', verify=False)

print(xyz)
