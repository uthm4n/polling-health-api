import requests
import time
import logging 
import sys
import json

polling_interval = input('How frequently (in seconds) would you like the API call to run?')
# if polling_interval = None:      # test implementation of a default polling interval 
#   polling_interval = 5
 #  break 
try:
    while True:
        url = "https://{YOUR-MORPHEUS-APPLIANCE-URL}/api/health"        # replace me with your Morpheus appliance URL (https://docs.morpheusdata.com/en/latest/getting_started/appliance_setup/appliance_setup.html)
        headers = {
            "accept": "application/json",
            "authorization": "Bearer {YOUR-API-TOKEN-HERE}"             # replace me with your API token - this can be generated on your appliance (Navigate to https://{YOUR-MORPHEUS-APPLIANCE-URL}/user-settings > API Access > Actions > morph-api > Regenerate) or read https://apidocs.morpheusdata.com/reference/updateusersettingsaccesstoken
            }
        response = requests.get(url, headers=headers, verify=False)
        string = response.json()
        print(json.dumps(string, indent=2))
        time.sleep({polling_interval})                                                   # poll every X seconds based on user input on line 7
except KeyboardInterrupt:                                               # runs indefinitely until a KeyboardInterrupt is triggered 
  logging.info("exiting...")
  sys.exit()
