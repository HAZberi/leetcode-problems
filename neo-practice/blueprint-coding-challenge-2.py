import requests  # type: ignore
import json

def fetch_data():
    response = requests.get("https://examples.lotworks.ca/interview/audrey-small.json")
    result = json.loads(response.text)
    return result

def sound_pattern(sound):
    allowed_pattern = [] #list of sets

    i = 0
    open = False
    while i < len(sound):
        if sound[i] == "(":
            open = True
            i += 1
        elif open == True:
            group = set()
            while sound[i] != ")":
                group.add(sound[i])
                i += 1
            allowed_pattern.append(group)
            open = False
            i += 1
        else:
            allowed_pattern.append(set([sound[i]]))
            i += 1
    
    return allowed_pattern

print(sound_pattern("(dc)(ba)"))

        
        




