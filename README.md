# Movie Ticket Availability Notifier

There have been times when I wanted to, but could not watch a movie on its first
weekend because I was late in booking the tickets. This crontask script will
notify you, when tickets to the target movie are available, so you never miss a
first-day-first-show again.

This is a Crontask for notification on availability of tickets for a new movie.

*BookMyShow is used for scraping availability, so check if your city has bookings through BMS before using.*

## Pre-requisites:
1. [Cron Jobs](https://awc.com.my/uploadnew/5ffbd639c5e6eccea359cb1453a02bed_Setting%20Up%20Cron%20Job%20Using%20crontab.pdf)
2. Python Libraries:-
    - bs4
    - requests
    - smtp
    - time
    - argparse (included by default)

## How to Use:

Fill up the below section in ```main.py``` before setting up the crontask.
This can be found at line 12 onwards.

```md
# FILL THIS UP OTHERWISE THE SCRIPT WON'T RUN
#################################################
# Login details of any gmail account
bot_mail = ''
password = ''
#################################################
```

Add the file path, date and time for running and excution command in ```crontab -e```.

```md
# For checking ticket availability every 15 minutes.

*/15 * * * * python3 $PATH_TO_SCRIPT/main.py -m [] -l [] example@email.com
```

**ADD THE COMMAND LINE ARGUMENTS BEFORE ADDING CRONJOB**. Help is given below.

```md
$ python3 movie.py -h
usage: main.py [-h] [-m [M]] [-l [L]] email

positional arguments:
  email       Email address to notify if tickets are available

optional arguments:
  -h, --help  show this help message and exit
  -m [M]      Name of movie to track
  -l [L]      Location where movie is tracked
```

<!--test3-->
For any queries mail me [here.](mailto:vivek.kaushal@outlook.com)
