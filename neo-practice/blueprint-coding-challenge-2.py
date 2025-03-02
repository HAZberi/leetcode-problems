import requests  # type: ignore
import json

def fetch_data():
    response = requests.get("https://examples.lotworks.ca/interview/audrey-small.json")
    result = json.loads(response.text)
    return result['Dictionary'], result['Sounds']

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

def count_possible_words(pattern, dictionary):
    count = 0

    for word in dictionary:
        if len(word) != len(pattern):
            continue
        match = True
        for char, char_pattern in zip(word, pattern):
            if char not in char_pattern:
                match = False
                break
        if match:
            count += 1
    
    return count

def main():
    dictionary, sounds = fetch_data()
    possible_words = []

    for sound in sounds:
        pattern = sound_pattern(sound)
        count = count_possible_words(pattern, dictionary)
        possible_words.append(count)

    print(possible_words)



main()
       
        




