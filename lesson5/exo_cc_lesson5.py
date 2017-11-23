import requests
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time


def getSoupFromURL(url, method='get', data={}):

    if method == 'get':
        res = requests.get(url)
    elif method == 'post':
        res = requests.post(url, data=data)
    else:
        return None
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None

url='http://www.open-medicaments.fr/api/v1/medicaments'

medicament = requests.get("http://www.open-medicamenticaments.fr/api/v1/medicamenticaments/" +                  str(code_medicament))
medicament = medicament.json()
denomination = str(medicament["denomination"]).split(" ")
nom = denomination[0]
labo = denomination[1]
actif = medicamenticament["compositions"][0]["substancesActives"][0]["dosageSubstance"] # a diviser par refer
prix = medicamenticament["presentations"][0]["prix"]
libelle = medicament["presentations"][0]["libelle"]


params={
    "query": "ibuprofene",
    "limit":10
}
res = requests.get("http://www.open-medicaments.fr/api/v1/medicaments", params=params)
res = res.json()
