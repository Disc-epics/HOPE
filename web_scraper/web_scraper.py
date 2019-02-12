#!/usr/bin/env python3.7

#######################################################
#import the libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#######################################################

def scrapSite():
    """
    Attempts to get the content on the Tippecanoe county inmate lsiting site (http://www3.tippecanoe.in.gov/InmateListing/InmateSearch.aspx)
    by making an HTTP GET request.
    :return: The HTML/XML text content of the county inmate lisitng site
    """

    #url variable declaration
    url = 'http://www3.tippecanoe.in.gov/InmateListing/InmateSearch.aspx'
    #This will return the html variable to raw_html
    raw_html = urlopen(url)

    #parse the html using beautiful soup and store it in variable 'html_content'
    #The variable talbe contial the table branch in the html that contians current inmates information.
    data = []
    html_content = BeautifulSoup(raw_html, 'html.parser')
    table = html_content.find('table', attrs={'cellspacing':'0'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            data.append(cols)
    with open('index.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for info in data:
            writer.writerow(info)
scrapSite()
