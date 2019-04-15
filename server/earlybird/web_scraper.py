#!/usr/bin/env python3
#######################################################
#import the libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
from earlybird.models import Client
from . import send_email
from . import send_text
#######################################################
clients = Client.objects.all()

def scrapeSite():
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
    
    #A list to tuples to hold current inmates names
    inmatesNames = []
    html_content = BeautifulSoup(raw_html, 'html.parser')
    table = html_content.find('table', attrs={'cellspacing':'0'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            inmatesNames.append((cols[2].capitalize(), cols[1].capitalize()))
    return inmatesNames
   
    
def checkStatus(inmatesNames, clients):
    """
    This functions takes in the a list of all the clients in our database and checks every to see if a client is in the current inmate list.
    If a client name appears in current inmate list then an email and text is sent to the right caseworker
    If a client name is the database but their name  no longer appears in the current inmate list then they are out of jail.
    """
    for client in clients:    
        if (client.first_name, client.last_name) in inmatesNames and client.status == False:
            emailBody = client.first_name + ' ' + client.last_name + ' was arrested.<br>For more details click here https://engineering.purdue.edu/earlybirdsystem/ </br> <br>Earlybird Systems</br>'
            textBody = client.first_name + ' ' + client.last_name + ' was arrested. For more details click here https://engineering.purdue.edu/earlybirdsystem/ Earlybird Systems'
            if client.user.email:
                send_email.send_email(client.user.email, 'Client Status Update', 'Your client ' + emailBody)
            if client.user.phone_number:
                send_text.send_text(client.user.phone_number, textBody)
            client.status = True
            client.save()
        elif client.status == True and (client.first_name, client.last_name) not in inmatesNames:
            body = client.first_name + ' ' + client.last_name + ' was released. <br>For more details click here https://engineering.purdue.edu/earlybirdsystem/</br> <br>Earlybird</br>'
            textBody = client.first_name + ' ' + client.last_name + ' was released. For more details click here https://engineering.purdue.edu/earlybirdsystem/ Earlybird Systems
            client.status = False
            client.save()
            send_email.send_email(client.user.email, 'Client Status Update', emailBody)
            send_text.send_text(client.user.phone_number, textBody)

def run_check():
    inmatesNames = scrapeSite()
    checkStatus(inmatesNames, clients) 
