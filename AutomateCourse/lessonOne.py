import pandas as pd
import os
os.environ['HTTP_PROXY'] = 'http://webproxy.bfm.com:8080'
os.environ['HTTPS_PROXY'] = 'https://webproxy.bfm.com:8080'

webPage=pd.read_html('https://en.wikipedia.org/wiki/The_Simpsons')
print(len(webPage))
print(webPage[1])