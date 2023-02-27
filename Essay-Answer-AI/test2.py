'''
l1 = []

with open('essay.txt') as article:
    for art in article:
        print(art)
        l1.append(art)

print()
print(l1)
'''

with open('essay.txt', 'w') as file:
    file.write('')

with open('essay.txt', 'a') as file:
    file.write('Aadit is was a King back in the olden days.\n')

with open('essay.txt', 'a') as file:
    file.write('Aadit is a fucking Emperor now!\n')

with open('essay.txt', 'a') as file:
    file.write('And will always remain')


