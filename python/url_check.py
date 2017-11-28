#!/usr/bin/env python

import sys, os, subprocess
import re

nagios_plugin="/usr/lib64/nagios/plugins/check_http"

url = ["https://etf.deutscheam.com/de-DE", "https://etf.deutscheam.com/GBR/ENG/Home", "https://etf.deutscheam.com/de-DE/produktfinder/?filters=%7b%22Asset+Class+Calculated%22:%5b%22Aktien%22%5d%7d&epslanguage=de-DE"]

for url in url:
    print (url)
    p1 = subprocess.Popen(["nagios_plugin", "-H etf.deutscheam.com -u url -S -f follow"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["re.search('HTTP.*1\.[01](.+?) OK .*', check_output).group(1)"], stdout=subprocess.PIPE)
    p2.communicate()




check_output = 'HTTP OK: HTTP/1.1 200 OK - 491717 bytes in 0.647 second response time |time=0.646803s;;;0.000000 size=491717B;;;0'

status_code = re.search('HTTP.*1\.[01](.+?) OK .*', check_output).group(1)
print(status_code)


#response_time = re.search('in (.+?) sec .* ', check_output).group(1)


#print (response_time)