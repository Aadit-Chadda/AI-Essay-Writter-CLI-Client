import requests

with open('reword-api-key.txt') as key:
    reword_api_key = key.readline()

with open('essay.txt') as art:
    essay = art.readline()

with open('essay.txt') as art:
    essay = art.readline()


url = "https://app.plaraphy.com/api/rewriter"

my_input = essay #"I can get lengthy response on topic xyz but when I paste exactly same prompt to api using davinci 003 I get like 70% shorter response, I tried everything I could, raising tokens, trying wtih 4000 and 2500, raising temps everything. Modyfing the prompt also didnt help its like the api is hard coded to limit the response? Any ideas on how i can get lentht response same or similar as one from chat gpt 3?"
payload = "text=" + my_input + ' &mode=fluent&lang=es&unique=true'
headers = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'authorization': 'Bearer ' + reword_api_key,
    'cache-control': 'no-cache',
}

response = requests.request('POST', url, data=payload, headers=headers)

res = response.json()
answer = res['rewrited']
print(answer)
#print(response.text)
