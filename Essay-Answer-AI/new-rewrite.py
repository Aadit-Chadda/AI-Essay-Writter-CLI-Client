import requests

with open('reword-api-key.txt') as key:
    reword_api_key = key.readline()


def paraphrasing():
    with open('final-essay.txt', 'w') as notepad:
        notepad.write('')

    with open('essay.txt') as article:
        art = article.readlines()

    url = "https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/"

    payload = {
        "text": art,
        "result_type": "multiple"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "6301683370msh192c3cadae42016p198b19jsna1cd72ed6b76",
        "X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)


paraphrasing()
