# Wifi-Analyser
Analyse the behaviour of connected wifi network.
The Wi-Fi Monitor script uses iwconfig for debian and netsh for windows commands to get the wifi name and signal strength.
Ping command is used to get the packet loss and latency of the network in either.
This data is saved in a csv file for later analysis.<br>
The common file imports the required libraries and common functions for the analyzers. It reads through the csv file in the case of any of the analyzers and asks the user to select the network to analyze  (the user might have been connected to different networks) the selected network is returned to the specific analyzer.<br>
The uptime analyzer plots a graph showing when the Wi-Fi was down and when it was up. The performance script plots a scatter to show how the network faired based on the packet loss and latency.
# Libraries
Pandas for reading and manipulating the csv data.<br>
Matplotlib for visualization.<br>

Leave the monitor script running for atleast a day for better analysis.
