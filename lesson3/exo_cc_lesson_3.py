from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from functools import reduce
import logging
import time
import csv


def getSoupFromURL(url):
    res = session.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None
        
def get_token(path):
    f = open(path, 'r')
    my_token = str(f.read())
    return my_token
    

def get_distance_matrix(cities):
    maps = googlemaps.Client(key=my_token)
    return maps.distance_matrix(origins=cities, destinations=cities)
    
df = pd.DataFrame(columns=cities, index=cities)
    for idx, row in enumerate(distance_matrix["rows"]):
        for idy, elem in enumerate(row["elements"]):
            df.at[cities[idx], cities[idy]] = elem["distance"]["text"]
    print(df)
