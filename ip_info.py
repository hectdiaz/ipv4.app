#!/bin/bash/python3

""" Welcome to our application! We have created this application to seamlessly view IPV4, IPV6 and location of the users!"""

import requests

def get_ip_info(api_key):
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

def main():
    api_key = '8d12eee976f4d115e89b3561b3d5fff4'
    ip_info = get_ip_info(api_key)
    if ip_info:
        print("IP Address:", ip_info.get('ip'))
        print("Country:", ip_info.get('country_name'))
        print("Type:", ip_info.get('type'))
    else:
        print("Failed to retrieve IP information.")

if __name__ == "__main__":
    main()
