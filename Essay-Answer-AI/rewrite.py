import requests
import time

with open('reword-api-key.txt') as key:
    reword_api_key = key.readline()


def rewording():
    with open('final-essay.txt', 'w') as notepad:
        notepad.write('')

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
            if "Your request has been created successfully" in answer:
                while True:
                    print('\n\nwaiting...')
                    time.sleep(12) #ToDo Find better way
                    response = requests.request('POST', url, data=payload, headers=headers)
                    res = response.json()
                    #print(response.text)
                    answer = res['rewrited']
                    if "Your request has been created successfully" in answer:
                        continue
                    else:
                        break


            with open('final-essay.txt', 'a') as ans:
                ans.write(answer)

            return answer

a = rewording()
print(a)

