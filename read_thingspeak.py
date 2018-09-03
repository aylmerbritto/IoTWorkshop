#!/usr/bin/env python

import urllib.request as ur
import json
import os
READ_API_KEY='QSQ7686F2F2I5IU2'
CHANNEL_ID= 567521
def main():
    conn = ur.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print("http status code=%s" %conn.getcode())
    response=response.decode()
    data=json.loads(response)
    print(data['field1'])
    print("")
    conn.close()

while True:
    main()
    


