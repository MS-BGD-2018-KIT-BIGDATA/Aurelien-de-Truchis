from bs4 import BeautifulSoup
import requests
import re
import json
import pandas as pd

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

def medicament(code_med):
    res = requests.get("http://www.open-medicaments.fr/api/v1/medicaments/" + str(code_med))
    med = res.json()
    denomination = str(med["denomination"]).split(" ")
    nom = denomination[0]
    labo = denomination[1]
    actif = med["compositions"][0]["substancesActives"][0]["dosageSubstance"] # a diviser par refer
    prix = med["presentations"][0]["prix"]
    libelle = med["presentations"][0]["libelle"]
    nb_comprimes = re.search(r'(\d{1,4})(?: comprim)', libelle)
    if nb_comprimes != None:
        nb_comprimes = nb_comprimes.group(1)
    else:
        nb_comprimes = re.search(r'(\d{1,4})(?: m?l)', libelle)
        if nb_comprimes != None:
            nb_comprimes = nb_comprimes.group(1)
    ligne = pd.DataFrame([nom, labo, actif, libelle, nb_comprimes], index=["nom", "labo", "actif", "libelle", "comprimes"])
    return ligne



params={
    "query": "ibuprofene",
    "limit":10
}
res = requests.get("http://www.open-medicaments.fr/api/v1/medicaments", params=params)
res = res.json()
