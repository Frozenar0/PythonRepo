import pandas as pd
from io import StringIO
import requests

#these are for blackrock proxy
import os
os.environ['HTTP_PROXY'] = 'http://webproxy.bfm.com:8080'
os.environ['HTTPS_PROXY'] = 'https://webproxy.bfm.com:8080'

#using requests.get and user agent to spoof python into thinking we are a browser,
#(??? this is my best understanding of it so far)
url = "http://www.football-data.co.uk/mmz4281/2122/E0.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

df = pd.read_csv(data, engine='python', sep='delimiter', header=None)
print(df)