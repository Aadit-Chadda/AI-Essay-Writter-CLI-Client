import os
import requests
import openai
import chatgpt
from chatgpt import *
from rewrite import *
from newRewrite import *

while True:
    prompt = input("Please Enter Your Question Here (To End Program Enter 'Q'): ")

    if prompt == 'Q' or prompt == 'q':
        break

    AI_answer = aiAnswer(prompt)

    print()

    print('AI Generated Answer:')
    print()
    print(AI_answer)

    #Reword_answer = rewording()
    Reword_answer = paraphrasing()

    print('\n\n')

    print('Human Reworded Answer')
    print()
    print(Reword_answer)

    print('\n\n')

print()
print('Program Ended')
print('*' * 30)
