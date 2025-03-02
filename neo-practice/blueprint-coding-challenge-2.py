import requests  # type: ignore
import json

def fetch_data():
    response = requests.get("https://examples.lotworks.ca/interview/audrey-small.json")
    result = json.loads(response.text)
    return result

print(fetch_data())
