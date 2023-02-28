import requests


def checkers():
    url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"

    with open('checker-api-key.txt') as api:
        key = api.read()

    with open('final-essay.txt') as art:
        article = art.read()

    total_l = len(article)
    if total_l > 3000:
        passage = article.split('.')
        l1 = []
        l2 = []
        count = 0
        answers = ""
        for i in passage:
            l1.append(i)
            count += 1
            if count == 30:
                for j in l1:
                    answers += j
                l2.append(answers)
                count = 0

        avg = []
        for i in l2:
            payload = {
                "text": i,
                "language": "en",
                "includeCitations": False,
                "scrapeSources": False
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": key,
                "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
            }

            response = requests.request("POST", url, json=payload, headers=headers)

            res = response.json()
            playPercent = res["percentPlagiarism"]
            avg.append(playPercent)
            #print(response.text)

        sumx = sum(avg)
        countx = len(avg)

        average = sumx/countx

        return average

    else:
        payload = {
            "text": article,
            "language": "en",
            "includeCitations": False,
            "scrapeSources": False
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        res = response.json()
        playPercent = res["percentPlagiarism"]

        #print(response.text)
        return playPercent


checkers()

