import json

output = {}

with open("words.txt") as file:
    for line in file:
        word = line.strip()
        letter = word[0]

        if letter not in output:
            output[letter] = [word]
        else:
            output[letter].append(word)

for l in output.values():
    l.sort()

with open("output.json", mode='w') as o:
    json.dump(output, o, indent=4, sort_keys=True)
