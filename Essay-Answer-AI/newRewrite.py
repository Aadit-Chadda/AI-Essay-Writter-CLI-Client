import requests

with open('reword-api-key.txt') as key:
    reword_api_key = key.readline()


def paraphrasing():
    answer = ""

    with open('final-essay.txt', 'w') as notepad:
        notepad.write('')

    with open('essay.txt') as article:
        arts = article.readlines()

    with open('new-rewording-api-key.txt') as api:
        key = api.read()

    for art in arts:
        my_input = art.replace('\n', '')
        if my_input == "":
            continue

        url = "https://rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com/rewrite"

        payload = {
            "language": "en",
            "strength": 3,
            "text": my_input,
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com",
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        #print(response.text)
        res = response.json()
        my_answer = res["rewrite"]
        answer += "\n" + my_answer

    with open('final-essay.txt', 'a') as ans:
        ans.write(answer)

    #print(answer)

    return answer


#paraphrasing()

