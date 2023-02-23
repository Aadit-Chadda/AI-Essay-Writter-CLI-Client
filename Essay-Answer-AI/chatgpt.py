import openai

with open('davincii-api-key.txt') as key:
    gpt_api_key = key.readline()


def aiAnswer(question):
    with open('essay.txt', 'w') as notepad:
        notepad.write('')

    openai.api_key = gpt_api_key

    response = openai.Completion.create(
        prompt=question,
        model="text-davinci-003",
        max_tokens=4000,
        temperature=0.7,
    )

    for result in response.choices:
        answer = result.text

    with open('essay.txt', 'w') as notebook:
        notebook.write(answer)

    return answer
