from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
import os
import mysql.connector
import random



connection_params = {
    'host': "localhost",
    'user': "zorg",
    'password': "zorg",
    'database': "bohrium_app_tmp",
}

request = "select id, nom from fuseau_horaire"

def liste_fuseaux(c) :
    c.execute("select id, nom from fuseau_horaire")
    resultats = c.fetchall()
    return resultats
    

with mysql.connector.connect(**connection_params) as db :
    with db.cursor() as c:
        liste_fuseaux = liste_fuseaux(c)
        
        for fuseau in liste_fuseaux :
            nom_fuseau = fuseau[1].lower().replace("/", "--")
            print(nom_fuseau)
            
            requete = "https://www.zeitverschiebung.net/en/timezone/"+nom_fuseau
            
            html = requests.get(requete, headers = {'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'})
            
            soup = BeautifulSoup(html.content, "html.perser")
            
            temps = random.random()
