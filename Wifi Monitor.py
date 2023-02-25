#!/usr/bin/env python
#Koome Frank
"""
Simple Python program that tracks the up/downtime of wifi network
The information is saved in a csv file for later analysis
The libraries used are: subprocess to execute ping command and read the ssid and signal
csv for working with csv files, datetime for time and date records, time for scheduling
and regex for searching within the returned string from subprocess.
"""

import subprocess
import csv
import datetime
import time
import re

#function to check and return the ssid and signal strength of the connected wifi
def wifi():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'interface'])
    result = result.decode('utf-8')
    result = result.replace('\r', '')

    #regular expression(regex) is used to search within the returned string 
    #the returned string is striped off whitespaces
    match_name = re.search('SSID (.*?)\n', result)
    ssid = match_name.group(1).strip(' :')
    match_signal = re.search('Signal(.*?)%', result)
    signal = match_signal.group(1).strip(' :')

    return ssid, signal

#function for trying to ping and return the packet loss and latency of the network
def ping(host):
    try:
        output = subprocess.check_output(['ping', '-n', '5', '-w', '1000', host])
        output = output.decode('utf-8')
        output = output.replace('\r', '')

        match_loss = re.search('\d+%\ loss', output)
        packet_loss = int(match_loss.group().strip(' loss%'))
        match_latency = re.search('Average = \d+', output)
        latency = int(match_latency.group().split('=')[1].strip())

        return packet_loss, latency
    except subprocess.CalledProcessError:
        pass

#define column names, create the csv file if it does not exist and add the first row
header = ["Network","Date","Time","Signal(%)","Status","Packet Loss(%)","Latency(ms)"]
filename = "wifi_statistics.csv"
try:
    with open(filename, "r") as file:
        read = csv.reader(file)
except FileNotFoundError:
    with open(filename, "w") as newfile:
        csvwriter = csv.writer(newfile) 
        csvwriter.writerow(header)

#run the script adding  the values to the csv at intervals of 100 seconds
while True:
    Date = datetime.date.today()
    Time = datetime.datetime.now().time().strftime("%H: %M: %S")
    def append():
        with open(filename,"a") as statsfile:
            csvwriter = csv.writer(statsfile)
            return csvwriter
    try:
        ssid, signal = wifi()
        packet_loss, latency = ping("google.com")
        append().writerow([ssid, Date, Time, signal, "up", packet_loss, latency])
    except TypeError:
        append().writerow([ssid, Date, Time, signal, "down"])
    except AttributeError:
        append().writerow(["Disconnected", Date, Time])
    time.sleep(100)