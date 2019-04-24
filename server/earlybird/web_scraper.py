#!/usr/bin/env python3
#######################################################
# import the libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
from earlybird.models import Client
from . import send_email
from . import send_text


#######################################################
#For any questions, 
#contact me at eadu@purdue.edu or eadu10261@gmail.com
#######################################################
#Clients contains all the clients in our database
clients = Client.objects.all()


def scrapeSite():
    """
    Attempts to get the content on the Tippecanoe county inmate lsiting site (http://www3.tippecanoe.in.gov/InmateListing/InmateSearch.aspx)
    by making an HTTP GET request.
    :return: The HTML/XML text content of the county inmate lisitng site
    """

    # url variable declaration
    url = 'http://www3.tippecanoe.in.gov/InmateListing/InmateSearch.aspx'
    
    # This will return the html variable to raw_html
    raw_html = urlopen(url)

    # A list to tuples to hold current inmates names
    inmatesNames = []

    # parse the html using beautiful soup and store it in variable 'html_content'
    html_content = BeautifulSoup(raw_html, 'html.parser')

    # The variable talbe contains the table branch in the html that contians current inmates information.
    table = html_content.find('table', attrs={'cellspacing': '0'})
    
    #Stores all rows of inmate data in a list
    rows = table.find_all('tr')
    
    #For Every row I extract the data booking #, last name, first name, middle name, booking date/time, and total bond amount.
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            #Stores the names of all current inmates name as a tuple into a list named inmatesNames
            inmatesNames.append((cols[2].capitalize(), cols[1].capitalize()))
    
    #Returns the current inmate list
    return inmatesNames


def checkStatus(inmatesNames, clients):
    """
    This functions takes in the a list of all the clients in our database and checks every to see if a client is in the current inmate list.
    If a client name appears in current inmate list then an email and text is sent to the right caseworker
    If a client name is the database but their name  no longer appears in the current inmate list then they are out of jail.
    """
    for client in clients:
        #Checks if a client in our data base who is currently not in jail name appears on the current inmate list. If it does, an alert is sent out
        if (client.first_name, client.last_name) in inmatesNames and client.status == False:
            emailBody = client.first_name + ' ' + client.last_name + \
                ' was arrested.<br>For more details click here https://engineering.purdue.edu/earlybirdsystem/ </br> <br>Earlybird System</br>'
            textBody = client.first_name + ' ' + client.last_name + \
                ' was arrested. For more details click here https://engineering.purdue.edu/earlybirdsystem/ Earlybird System'
            #updates client status.
            client.status = True
            client.save()
            
            # Only send an email if the caseworker provided an email
            if client.user.email:
                send_email.send_email(
                    client.user.email, 'Client Status Update', 'Your client ' + emailBody)
            
            # Only send text if caseworker provided a phone number
            if client.user.phone_number:
                send_text.send_text(client.user.phone_number, textBody)
        
        #If client is in jail and client name no longer appears on the current inmate list, imate is free  
        elif client.status == True and (client.first_name, client.last_name) not in inmatesNames:
            emailBody = client.first_name + ' ' + client.last_name + \
                ' was released. <br>For more details click here https://engineering.purdue.edu/earlybirdsystem/</br> <br>Earlybird System</br>'
            textBody = client.first_name + ' ' + client.last_name + \
                ' was released. For more details click here https: // engineering.purdue.edu/earlybirdsystem / Earlybird System'
            
            #Updates and saves client status 
            client.status = False
            client.save()
            
            if client.user.email:
                send_email.send_email(
                    client.user.email, 'Client Status Update', emailBody)
            if client.user.phone_number:
                send_text.send_text(client.user.phone_number, textBody)


def run_check():
    """
        This program runs everything
    """
    inmatesNames = scrapeSite()
    checkStatus(inmatesNames, Client.objects.all())
