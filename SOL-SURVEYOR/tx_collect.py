from datetime import datetime, date
import requests
import time
import pandas
import json

def pull_transactions():
    #Set datetime at time of running script (in unix for calcs)
    unix_current = int(datetime.now().timestamp())
    print("The current time is {}".format(unix_current))
    #Set unix datetime a minute prior to running script
    unix_minute_ago = int(unix_current - 60*1000)
    print("The time one minute ago was {}".format(unix_minute_ago))
    #Set wallet to be the Magic Eden program address
    wallet = "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix"
    #Make request to solscan API

def convert_to_json_obj():
    pass
