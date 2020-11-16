import json

import requests

def mental_health_data_scrape():
    response = requests.get("https://data.cdc.gov/resource/8pt5-q6wp.json")
    data = json.loads(response.text)
    return data
print(mental_health_data_scrape())

if __name__ == '__main__':
    mental_health_data_scrape()
    