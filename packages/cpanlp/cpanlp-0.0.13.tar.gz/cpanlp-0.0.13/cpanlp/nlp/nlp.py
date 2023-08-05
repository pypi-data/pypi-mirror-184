import jieba
import requests
import pdfplumber
import urllib
import json
import pandas as pd
def gettoday():
    url = "https://hhzjp3y4p6pjfqbkkbhzwgyoqa0ngqep.lambda-url.ap-southeast-1.on.aws/"
    ww=[]
    response = urllib.request.urlopen(url)
    a = response.read().decode('utf-8')
    df = pd.read_json(a)
    return df    
class nlpaccounting:
    def __init__(self):
        pass

    def tokenize(self, text):
        return jieba.cut(text)
