'''
BMS-notifiier
Version-1-CRONTASK

14.7.2018

A notification system to check for when tickets are available for a new movie.
CRONTASK
@kaushalvivek
'''

# FILL THIS UP OTHERWISE THE SCRIPT WON'T RUN
#################################################
# Login details of any gmail account
bot_mail = ''
password = ''
#################################################


import argparse
from bs4 import BeautifulSoup as bs
import requests
import smtplib
import time


parser = argparse.ArgumentParser()
parser.add_argument("-m", nargs="?", help="Name of movie to track", type=str)

parser.add_argument("-l", nargs="?", help="Location where movie is tracked",
                    type=str)

parser.add_argument("email", help="Email address to notify if tickets are \
                    available", type=str)
args = parser.parse_args()

if args.m and args.l and args.email and bot_mail and password:
    pass
else:
    print("Enter all the arguments\n")
    print(parser.print_help())
    quit()


def search(mov, loc):
    req = requests.get('https://www.google.co.in/search?q=bms '+loc+' '+mov)
    soup = bs(req.text, 'html.parser')
    tags = soup.findAll('h3')
    for i in range(3):
        analyse(tags[i].a.attrs['href'], mov, loc)


def mail(mov, loc):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(bot_mail, password)
    SUBJECT = "bms_alert " + mov + " " + loc
    TEXT = "Hi Human, \n\nTickets for {} are for sale in {}. Cheers!\n\nYours, \nLab PC".format(mov, loc)
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    server.sendmail(bot_mail, args.email, msg)
    server.quit()


def analyse(link, mov, loc):
    if 'buytickets' in link:
        mail(mov, loc)
        quit()


link = search(args.m, args.l)
