import os
import requests
import openai

with open('essay.txt', 'w') as notepad:
    notepad.write('')

with open('davincii-api-key.txt') as key:
    gpt_api_key = key.readline()

with open('reword-api-key.txt') as key:
    reword_api_key = key.readline()


def aiAnswer(question):
    openai.api_key = gpt_api_key

    response = openai.Completion.create(
        prompt=question,
        model="text-davinci-003",
        max_tokens=4000,
        temperature=0.7,
    )

    for result in response.choices:
        answer = result.text

    return answer


prompt = input("Please Enter Your Question: ")

AI_answer = aiAnswer(prompt)

print('AI Generated Answer: ')
print(AI_answer)

with open('essay.txt', 'w') as notepad:
    notepad.write(AI_answer)

print()
print("*" * 30)

