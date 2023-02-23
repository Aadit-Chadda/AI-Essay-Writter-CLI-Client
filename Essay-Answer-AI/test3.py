import requests

with open('reword-api-key.txt') as key:
    reword_api_key = key.readline()

with open('essay.txt') as article:
    l1 = []
    for art in article:
        l1.append(art)

for line in l1:
    url = "https://app.plaraphy.com/api/rewriter"

    my_input = line.replace('\n', '')
    if my_input == '':
        pass
    else:
        payload = "text=" + my_input + ' &mode=fluent&lang=es&unique=true'
        headers = {
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'authorization': 'Bearer ' + reword_api_key,
            'cache-control': 'no-cache',
        }

        response = requests.request('POST', url, data=payload, headers=headers)

        res = response.json()
        #print(response.text)
        answer = res['rewrited']
        print(answer)