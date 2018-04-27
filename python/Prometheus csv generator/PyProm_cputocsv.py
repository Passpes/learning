import csv
import requests
import sys
import datetime
import time

"""
A simple program to print the result of a Prometheus query_range "win_cpu_Percent_Processor_Time"  as CSV.

By Oucema Bellagha
"""


#fromdate = (str(raw_input("Starting date: ")))
#todate = (str(raw_input("End date: ")))
#
fromdate = (time.mktime(datetime.datetime.strptime((str(raw_input("Starting date: "))), "%d/%m/%Y %H:%M").timetuple()))
todate = (time.mktime(datetime.datetime.strptime((str(raw_input("End Date: "))), "%d/%m/%Y %H:%M").timetuple()))

print(fromdate)
print(todate)


urls ={
       "Web030":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate),
       "Web031":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate),
       "App003":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate),
       "App004":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate),
       "App005":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate),
       "App006":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate),
       "SHOneVM003":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate),
       "SHOneVM004":"http://localhost:9090/api/v1/query_range?query=avg_over_time(win_cpu_Percent_Processor_Time{instance=~\"x.x.x.x:9273\",job=\"windows\"}[15m])&start=%s&end=%s&step=900"% (fromdate,todate)}

for url in urls:
    print(urls[url])

for url in urls:
    response = requests.get(urls[url])
    x = response.json()['data']['result']
    f = csv.writer(open("etf_cpu.csv", "a"))
#    f = csv.writer(open(url+"_mem.csv", "wb+"))
    f.writerow(["host","instance","job","objectname","values"])
    for x in x:
        f.writerow([x["metric"]["host"],
                    x["metric"]["instance"],
                    x["metric"]["job"],
                    x["metric"]["objectname"],
                    x["values"]])
