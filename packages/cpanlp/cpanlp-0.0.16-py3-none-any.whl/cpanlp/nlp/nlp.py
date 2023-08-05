import jieba
import requests
import pdfplumber
import urllib
import pandas as pd
from io import BytesIO
import re
def gettoday():
    url = "https://q5xsbdueopbmh7oykiyrjsjq240rjmgu.lambda-url.ap-southeast-1.on.aws"
    ww=[]
    response = urllib.request.urlopen(url)
    a = response.read().decode('utf-8')
    df = pd.read_json(a)
    df.rename(columns={
    'mch': '标题',
    'zhqdm': '证券代码',
    'zhqjc':'证券简称',
    'ggbh':'网址',
    'riqi':'日期'}, inplace=True)
    df.drop('name', axis=1, inplace=True)
    return df    
class nlpaccounting:
    def __init__(self):
        pass
    def tokenize(self, text):
        return jieba.cut(text)
def getreport(url: str):
    req = requests.get(url)
    with pdfplumber.open(BytesIO(req.content)) as pdf:
     a=""
     for page in pdf.pages:
         text = page.extract_text()
         a=a+text
    a=re.sub(r"\n", '', a)
    a=re.sub(r" ", '', a)
    a = re.sub(r"\.{5,}", '', a)
    return a