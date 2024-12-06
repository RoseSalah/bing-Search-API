import json
import os
from pprint import pprint
import requests

os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY'] = '802e628099094ea48ddfb5f55aea53ed'  
os.environ['BING_SEARCH_V7_ENDPOINT'] = 'https://api.bing.microsoft.com'

subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] + "/v7.0/search" #+ "/bing/v7.0/search" => causes 404 resource not found error

# Query term to search for. 
query = "Microsoft Cognitive Services"

# Construct a request
mkt = 'en-US'
params = {'q': query, 'mkt': mkt}
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Call the API
try:
    response = requests.get(endpoint, headers=headers, params=params)
    print(f"Requesting URL: {response.url}")
    response.raise_for_status()
    print("\nHeaders:\n")
    print(response.headers)
    print("\nJSON Response:\n")
    pprint(response.json())
    # print("ALL DONE GIRL")
except Exception as ex:
    print("An error occurred:", ex)
