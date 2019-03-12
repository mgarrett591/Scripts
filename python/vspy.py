import sys
import math
import time
import datetime
import random
import matplotlib as mplot
import numpy as np
import pint
import webbrowser
pi=math.pi
e=math.e
def test():
    return 'A function has been called!'
def src():
    file=open('vspy.py','r')
    file=file.read()
    return file
def getTimeStamp(date):
    if(date.find('-')>0):
        return time.mktime(datetime.datetime.strptime(date, "%m-%d-%Y").timetuple())
    elif(date.find('/')>0):
        return time.mktime(datetime.datetime.strptime(date, "%m/%d/%Y").timetuple())
def timeSince(date):
         then=getTimeStamp(date)
         now=time.time()
         delta=(now-then)/31540000
         return int(math.floor(delta))
def dice(sides=6):
    return random.randint(1, sides)
def getAge(name):
    name=name.lower()
    bdays={'mark':'10/1/1997',
    'sarah':'1/11/1995',
    'daniel':'7/31/1993',
    'iva':'2/7/1993',
    'ruby':'11/22/1995',
    'warren':'7/23/1995',
    'dad':'7/17/1966',
    'mom':'10/28/1968',
    'grandma':'12/25/1939',
    'granddad':'1/18/1939',
    'memaw':'9/24/1944',
    'pawpaw':'12/1/1943',
    'tomas':'7/26/1995',
    'jenifer':'11/18/1987',
    'david':'11/28/1964',
    'john':'1/22/1968',
    'beth':'2/3/1961',
    'charles':'7/14/1969',
    'auntstephonie':'0/0/0',
    'natalie':'0/0/0',
    'megan':'0/0/0',
    'lstephonie':'0/0/0',
    'victoria':'0/0/0',
    'christopher':'0/0/0',
    'madaline':'0/0/0'}
    return timeSince(str(bdays[name]))
def web(url):
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
#put all new functions above this line.
prin
