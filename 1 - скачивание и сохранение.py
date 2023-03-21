import json, urllib.request
import base64

import datetime

date = str(datetime.date.today())

periods = ['week', 'month', '3month']

for period in periods:
    print (f'downloading ... {period}')
    js = json.load(urllib.request.urlopen(f'https://trending-searches.wb.ru/file?period={period}'))
    if (js['error'] == False):
        data = base64.b64decode(js['data']['file'])
        fp = open(f"data-{period}/wbqueries-{period}-{date}.csv", "wb")
        fp.write(data)
    else:
        print (f'ERROR downloading ... {period}')