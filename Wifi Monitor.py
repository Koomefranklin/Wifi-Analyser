#!/usr/bin/env python
import subprocess
import csv
import datetime
import time

def wifi():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'interface'])
    result = result.decode('utf-8')
    result = result.replace('\r', '')

    ssid = result.split('\n')[8].split(':')[1].strip()
    signal = result.split('\n')[18].split(':')[1].strip()

    return ssid, signal

def ping(host):
    try:
        output = subprocess.check_output(['ping', '-n', '5', '-w', '1000', host])
        output = output.decode('utf-8')
        output = output.replace('\r', '')

        latency = output.split("\n")[11].split(",")[2].split("=")[1].strip(' ms')
        Packet_loss = output.split("\n")[9].split("(")[1].strip(' loss),%')

        return Packet_loss, latency
    except subprocess.CalledProcessError:
        pass

header = ["Network","Date","Time","Signal(%)","Status","Packet Loss(%)","Latency(ms)"]

try:
    with open("wifi_statistics.csv", "r") as file:
        read = csv.reader(file)
except FileNotFoundError:
    with open("wifi_statistics.csv", "w") as newfile:
        csvwriter = csv.writer(newfile) 
        csvwriter.writerow(header)

while True:
    try:
        ssid, signal = wifi()
        packet_loss, latency = ping("google.com")
        Date = datetime.date.today()
        Time = datetime.datetime.now().time().strftime("%H: %M: %S")

        with open("wifi_statistics.csv","a") as statsfile:
            csvwriter = csv.writer(statsfile)
            csvwriter.writerow([ssid, Date, Time, signal, "up", packet_loss, latency])
    except TypeError:
        with open("wifi_statistics.csv","a") as statsfile:
            csvwriter = csv.writer(statsfile)
            csvwriter.writerow([ssid, Date, Time, signal, "down"])
    except ValueError:
        pass
    time.sleep(300)