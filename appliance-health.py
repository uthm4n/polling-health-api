import requests
import time
import logging 
import sys
import json

polling_interval = input('How frequently (in seconds) would you like the API call to run?')
morpheus_node = input('Which Morpheus node would you like to get the health for?')
morph_api_key = input('What is your Morpheus API (morph-api) key?')                           # Administration > User Settings > API Access 

try:
    while True:
        url = f"https://{morpheus_node}/api/health"        # node = the hostname of your appliance node. In a HA environment, you have multiple nodes so you can specify here which one you want to retrieve the health for. You can provide the hostname or IP address when prompted for input 
        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {morph_api_key}"            # make sure an API token is generated for morph-api on your appliance (Navigate to https://{YOUR-MORPHEUS-APPLIANCE-URL}/user-settings > API Access > Actions > morph-api > Regenerate) or read https://apidocs.morpheusdata.com/reference/updateusersettingsaccesstoken
            }
        response = requests.get(url, headers=headers, verify=False)
        string = response.json()
        print(json.dumps(string, indent=2))
        print(f"Waiting for {polling_interval} seconds before triggering the next call...") 
        time.sleep(int(polling_interval))                                                   # poll every X seconds based on user input on line 7
except KeyboardInterrupt:                                               # runs indefinitely until a KeyboardInterrupt is triggered 
  logging.info("exiting...")
  sys.exit()
