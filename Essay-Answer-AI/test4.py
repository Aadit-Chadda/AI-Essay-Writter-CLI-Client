import requests

with open('reword-api-key.txt') as key:
    reword_api_key = key.readline()

with open('essay.txt') as article:
    l1 = []
    for art in article:
        l1.append(art)

for line in l1:
    my_input = line.replace('\n', '')
    if my_input == '':
        pass
    else:
        payload = "text=" + my_input + ' &mode=fluent&lang=es&unique=true'
        print(payload)
    print()
