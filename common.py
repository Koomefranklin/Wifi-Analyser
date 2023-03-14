#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt


def specifyNetwork():
    # Read CSV file into a DataFrame
    df = pd.read_csv("wifi_statistics.csv")

    #drop rows without values in the status column
    df = df.loc[df['Status'] != None]

    networks = df["Network"].unique() # get a list of the connected networks

    # create a new list excluding the disconnected times
    registered_networks = []
    for network in networks:
        if network != "None":
            registered_networks.append(network)

    # get the user to pick a network to analyse
    # using try statement to ask for input again if the input is not an int or is out of range
    print("Connected Networks")
    net_number = 1
    for value in registered_networks:
        print(f'{net_number}. {value}')
        net_number += 1

    def verifyInput():
        try:
            selected_index = int(input('Select the network to analyze by number: '))
            selected_network = registered_networks[selected_index-1]
            return selected_network
        except (ValueError, IndexError):
            print("Wrong input try again\n")
            return verifyInput()
        
    user_selection = verifyInput()    
    print(f"Analyzing {user_selection}")

    # create a new dataframe comprising of only the selected network
    df = df.loc[df['Network'] == user_selection]
    
    # return the network ssid and the dataframe
    return user_selection, df