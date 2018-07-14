# Movie Ticket Availability Notifier
This is a Crontask for notification on availability of tickets for a new movie.<br />
*BookMyShow is used for scraping availability, so check if your city has bookings through BMS before using.*

## Pre-requisites:
1. [Crontasks](https://awc.com.my/uploadnew/5ffbd639c5e6eccea359cb1453a02bed_Setting%20Up%20Cron%20Job%20Using%20crontab.pdf)
2. Python Libraries:-
    - bs4
    - requests
    - smtp
    - time

## How to Use:

Fill up the below section in ```main.py``` before setting up the crontask:
```
####################################

# Enter before execution:

# Name of the movie to be searched
mov = ''

# City where you want to search for ticket availability
loc = ''

# Login details of bot's gmail account
bot_mail = ''
password =''

# Email address where you want to be notified
target_mail = ''

####################################
```
<!--test3-->
For any queries mail me [here.](mailto:vivek.kaushal@outlook.com)
