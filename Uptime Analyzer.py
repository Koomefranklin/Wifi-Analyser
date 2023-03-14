#!/usr/bin/env python
# coding: utf-8

# import everything from the file with the common codes
from common import *

network, df = specifyNetwork() # the returned values from the common file

# Convert date and time columns to a single datetime column
df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# Set datetime column as the DataFrame index
df = df.set_index('datetime')

# get nuptime number and total time
num_uptime_minutes = (df['Status'] == "up").sum()
total_minutes = len(df)

uptime_percentage = num_uptime_minutes / total_minutes * 100

#plot graph of Status against time
plt.plot(df.index, df['Status'])

# Print the average uptime percentage for the entire period
plt.title(f"Up/Down time analysis for {network}\nAverage uptime percentage: {format(uptime_percentage.mean(),'.2f')}%")

# Set the x and y-axis labels
plt.xlabel('Time')
plt.xticks(rotation=45)
plt.ylabel('Status')

plt.show()