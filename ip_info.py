#!/bin/bash/python3

""" Welcome to our application! We have created this application to seamlessly view IPV4, IPV6 and location of the users!"""

import requests

def get_ip_info(api_key):                 #This is defining the API, ensuring this API works with the provided key
    url = f'http://api.ipstack.com/check'
    params = {'access_key': api_key}

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():                                    #this is defining the main code using we define the API key here
    api_key = '8d12eee976f4d115e89b3561b3d5fff4'
    ip_info = get_ip_info(api_key)
    if ip_info:
        print("IP Address:", ip_info.get('ip')) #This is requesting the IP address of the current user
        print("Country:", ip_info.get('country_name')) #The feature pulls the country of the user
        print("Type:", ip_info.get('type')) #This shows the type of connection, whether an IPV4 or IPV6
        print("You are located in the state of ", ip_info.get('region_name')) #shows the state that the user is currently in
    else:
        print("Failed to retrieve IP information.") #This gives us a failure if the code is run without any IP addressing information

if __name__ == "__main__":
    main()
