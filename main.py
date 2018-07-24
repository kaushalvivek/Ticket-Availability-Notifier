'''
BMS-notifiier
Version-1-CRONTASK

14.7.2018

A notification system to check for when tickets are available for a new movie.
CRONTASK
@kaushalvivek
'''

from bs4 import BeautifulSoup as bs
import requests
import smtplib
import time

####################################

# Enter before execution:

# Name of the movie to be searched
mov = ''

# City where you want to search for ticket availability
loc = ''

# Login details of any gmail account
bot_mail = ''
password =''

# Email address where you want to be notified
target_mail = ''

####################################

# def input_movie():
#     movie = input('Enter movie to lookout for: ')
#     return movie
    
# def input_location():
#     location = input('Enter city to search in: ')
#     return location

def search(mov,loc):
    req = requests.get('https://www.google.co.in/search?q=bms '+loc+' '+mov)
    soup = bs(req.text,'html.parser')
    tags = soup.findAll('h3')
    for i in range (3):
        analyse(tags[i].a.attrs['href'],mov,loc)

def mail (mov,loc):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(bot_mail, password)
    SUBJECT = "bms_alert "+mov+" "+loc
    TEXT = "Hi Human,\n\nTickets for "+mov+" are now on sale in "+loc+".\n Cheers!\n\nYours,\nLab PC"
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT) 
    server.sendmail(bot_mail, target_mail, msg)
    server.quit()

def analyse(link,mov,loc):
    if 'buytickets' in link:
        mail(mov,loc)
        quit()
    
link = search(mov,loc)
    
