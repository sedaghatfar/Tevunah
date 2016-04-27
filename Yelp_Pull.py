# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:58:57 2016

@author: Matt
"""

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import pandas as pd
import numpy as np
from pandas import ExcelWriter

data = pd.ExcelFile('Yelp_Phone.xlsx')

df = data.parse('MyData')

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)


client = Client(auth)


print "Start"

columns = ['phone','name', 'review_count', 'categories','rating']


new = []
j = 0

for i in df['SearchPhone'][:5000]:
    print i, j, j/5000.0
    try:
        response = client.phone_search("'" + str(i) + "'")
        new.append([response.businesses[0].phone
                ,response.businesses[0].name
                ,response.businesses[0].review_count
                ,response.businesses[0].categories
                ,response.businesses[0].rating])
    except IndexError:
        new.append([str(i),"","","",""])
    else:
        new.append([str(i),"","","",""])
    j += 1
        
df2 = pd.DataFrame(new)

        
df2.to_csv("Yelp5000.csv", index=False, header=False)


print "end"

