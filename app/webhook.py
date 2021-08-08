import requests 
import json  
import pandas as pd 
import os 

from urllib.request import urlopen 
from bs4 import BeautifulSoup 

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  
APP_STATIC = os.path.join(APP_ROOT, 'static')

# URL = "https://webhook.site/9000beca-9c95-4774-8b70-72ef52460ff4" 
URL = 'http://127.0.0.1:5000/webhook' 

sample_data = {'a': 'b', 'c': 'd'}

url = "https://www.naver.com" 
res = requests.get(url) 
html = BeautifulSoup(res.content, 'html.parser') 
sample_data = {'content': str(html)}

with open(os.path.join(APP_STATIC, 'data.json'), 'r') as file:
    inpt_data = json.load(file)

inpt_data.append(sample_data)
 
with open(os.path.join(APP_STATIC, 'data.json'), 'w') as file:
    json.dump(inpt_data, file) 

r = requests.post(URL, data=json.dumps(inpt_data)) 