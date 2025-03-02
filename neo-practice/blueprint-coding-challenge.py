import requests  # type: ignore
import json

# result output -> https://examples.lotworks.ca/interview/teammates-bp-output.txt
# question -> https://examples.lotworks.ca/interview/teammates.txt

def fetch_data():
    response = requests.get('https://examples.lotworks.ca/interview/teammates.json')
    result = json.loads(response.text)
    return result

def extract_data(teammates: list):
    return list(map(lambda x: {'Name': x['Name'], 'Address': {'StreetName': x['Address']['StreetName'], 'StreetNumber': int(x['Address']['StreetNumber'])} }, teammates))

def sort_data(teammates: list):
    return sorted(teammates, key=lambda x: (x['Address']['StreetName'], x['Address']['StreetNumber']))

def format_data(teammates: list):
    res = ["Name, Address"]
    for teammate in teammates:
        res.append(f"{teammate['Name']}, {teammate['Address']['StreetNumber']} {teammate['Address']['StreetName']}")
    
    return "\n".join(res)


# Execution
print(format_data(sort_data(extract_data(fetch_data()['Team']))))




