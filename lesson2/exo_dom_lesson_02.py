{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>= Besoin ou capacité de financement de la section d'investissement = E</th>\n",
       "      <th>Besoin ou capacité de financement Résiduel de la section d'investissement = D - C</th>\n",
       "      <th>RESULTAT COMPTABLE = A - B = R</th>\n",
       "      <th>Résultat d'ensemble = R - E</th>\n",
       "      <th>TOTAL DES CHARGES DE FONCTIONNEMENT = B</th>\n",
       "      <th>TOTAL DES EMPLOIS D'INVESTISSEMENT = D</th>\n",
       "      <th>TOTAL DES RESSOURCES D'INVESTISSEMENT = C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>En milliers d Euros</th>\n",
       "      <td>322767</td>\n",
       "      <td>2801912</td>\n",
       "      <td>4964789</td>\n",
       "      <td>325230</td>\n",
       "      <td>5425200</td>\n",
       "      <td>2479145</td>\n",
       "      <td>460411</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Euros par habitant</th>\n",
       "      <td>146</td>\n",
       "      <td>1265</td>\n",
       "      <td>2241</td>\n",
       "      <td>147</td>\n",
       "      <td>2449</td>\n",
       "      <td>1119</td>\n",
       "      <td>208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moyenne de la strate</th>\n",
       "      <td>146</td>\n",
       "      <td>1265</td>\n",
       "      <td>2241</td>\n",
       "      <td>147</td>\n",
       "      <td>2449</td>\n",
       "      <td>1119</td>\n",
       "      <td>208</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                      = Besoin ou capacité de financement de la section d'investissement = E  \\\n",
       "En milliers d Euros                                              322767                        \n",
       "Euros par habitant                                                  146                        \n",
       "Moyenne de la strate                                                146                        \n",
       "\n",
       "                      Besoin ou capacité de financement Résiduel de la section d'investissement = D - C  \\\n",
       "En milliers d Euros                                             2801912                                   \n",
       "Euros par habitant                                                 1265                                   \n",
       "Moyenne de la strate                                               1265                                   \n",
       "\n",
       "                      RESULTAT COMPTABLE = A - B = R  \\\n",
       "En milliers d Euros                          4964789   \n",
       "Euros par habitant                              2241   \n",
       "Moyenne de la strate                            2241   \n",
       "\n",
       "                      Résultat d'ensemble = R - E  \\\n",
       "En milliers d Euros                        325230   \n",
       "Euros par habitant                            147   \n",
       "Moyenne de la strate                          147   \n",
       "\n",
       "                      TOTAL DES CHARGES DE FONCTIONNEMENT = B  \\\n",
       "En milliers d Euros                                   5425200   \n",
       "Euros par habitant                                       2449   \n",
       "Moyenne de la strate                                     2449   \n",
       "\n",
       "                      TOTAL DES EMPLOIS D'INVESTISSEMENT = D  \\\n",
       "En milliers d Euros                                  2479145   \n",
       "Euros par habitant                                      1119   \n",
       "Moyenne de la strate                                    1119   \n",
       "\n",
       "                      TOTAL DES RESSOURCES D'INVESTISSEMENT = C  \n",
       "En milliers d Euros                                      460411  \n",
       "Euros par habitant                                          208  \n",
       "Moyenne de la strate                                        208  "
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Created on Mon Sep 25 12:21:40 2017\n",
    "\n",
    "@author: auredt7892\n",
    "\"\"\"\n",
    "import requests\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def getSoupFromURL(url, method='get', data={}):\n",
    "\n",
    "  if method == 'get':\n",
    "    res = requests.get(url)\n",
    "  elif method == 'post':\n",
    "    res = requests.post(url, data=data)\n",
    "  else:\n",
    "    return None\n",
    "\n",
    "  if res.status_code == 200:\n",
    "    soup = BeautifulSoup(res.text, 'html.parser')\n",
    "    return soup\n",
    "  else:\n",
    "    return None\n",
    "\n",
    "def createDic (ListOfString, ListOfInt3x):\n",
    "    Dic = {}\n",
    "    for i in range(1,len(ListOfString)):\n",
    "        Dic[ListOfString[i]] = [ListOfInt3x[3*i-3] , ListOfInt3x[3*i-2] , ListOfInt3x[3*i-1]]\n",
    "    return(Dic)\n",
    "\n",
    "def getDataFrameforYear (Year):\n",
    "    \n",
    "    soup = getSoupFromURL('http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice='+ Year)\n",
    "    Montants = soup.find_all(class_ = \"montantpetit G\")\n",
    "    IntituléMontants = soup.find_all(class_ = \"libellepetit G\")\n",
    "    ListeIntituléMontants = list(map(lambda x: x.get_text(), IntituléMontants))\n",
    "    ListeMontants = list(map(lambda x: int(x.get_text().replace(u'\\xa0' or u' ', u'').replace(u' ' or u' ', u'')), Montants ))\n",
    "    Dic = createDic(ListeIntituléMontants,ListeMontants)\n",
    "    DataFrame = pd.DataFrame(Dic, index=['En milliers d Euros','Euros par habitant','Moyenne de la strate'])\n",
    "    return(DataFrame)\n",
    "    \n",
    "getDataFrameforYear('2010')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}