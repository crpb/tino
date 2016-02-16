#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import ast

webpage = "http://www.dwd.de/DE/wetter/wetter_weltweit/europa/wetterwerte/_node.html"

try:
    web_page = urllib2.urlopen(webpage)

except urllib2.HTTPError:
    print("HTTPERROR!")
except urllib2.URLError:
    print("URLERROR!")

if web_page:
    soup = BeautifulSoup(web_page,'lxml')
    soup.prettify('utf-8')
    c = soup.find('div', {'id':'wettertab'})
    e = c.find('tbody')

    results = {}
    for row in e.findAll('tr'):
        aux = row.findAll('td')
        stadt = str(aux[0].contents[0].strip().encode("utf-8"))
        results[stadt] = {}
        results[stadt]['hoehe'] = aux[1].contents[0].strip().encode("utf-8")
        results[stadt]['luftdruck'] = aux[2].contents[0].strip().encode("utf-8")
        results[stadt]['temperatur'] = aux[3].contents[0].strip().encode("utf-8")
        results[stadt]['windspitzen'] = aux[4].contents[0].strip().encode("utf-8")
        results[stadt]['windrichtung'] = aux[5].contents[0].strip().encode("utf-8")
        results[stadt]['windgeschwindigkeit'] = aux[6].contents[0].strip().encode("utf-8")
        results[stadt]['wolken'] = aux[7].contents[0].strip().encode("utf-8")
        results[stadt]['boehen'] = aux[8].contents[0].strip().encode("utf-8")

for stadt in results:
    print stadt, 'Daten ', results[stadt]
