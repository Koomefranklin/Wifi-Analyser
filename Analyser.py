#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame
df = pd.read_csv("wifi_statistics.csv")

#drop rows without values in the status column
df = df.loc[df['Status'] != None]

# Convert date and time columns to a single datetime column
df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# Set datetime column as the DataFrame index
df = df.set_index('datetime')

# Calculate the number of minutes between each measurement
time_diffs = df.index.to_series().diff().dt.total_seconds() / 60

# Calculate the number of uptime minutes and total minutes removing the time it was disconnected
num_uptime_minutes = (df['Status'] == 'up').resample('1H').sum()
disonnected_minutes = (df['Status'] == 'Disconnected').resample('1H').sum()
num_total_connected_minutes = time_diffs.resample('1H').sum() - disonnected_minutes

# Calculate the uptime percentage for each hour
uptime_percentage = num_uptime_minutes / num_total_connected_minutes * 100

#plot graph of status against time
plt.plot(df.index, df['Status'])

# Print the average uptime percentage for the entire period
plt.text("Average uptime percentage: {:.2f}%".format(uptime_percentage.mean()))
# Set the x and y-axis labels
plt.xlabel('Time')
plt.ylabel('Status')

plt.show()