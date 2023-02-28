


string = "Lambskin condoms: These. condoms are made. from the intestinal. membrane of a lamb and. are highly effective. at preventing pregnancy. However, they may not offer protection. against certain STIs, including HIV."

a = string.rfind('.')
print(a)
print(len(string))

al = string.split('.')
l1 = []
l2 = []
count = 0
answers = ""
for i in al:
    l1.append(i)
    count += 1
    if count == 3:
        count = 0
        for j in l1:
            answers += j
        l2.append(answers)

print(l2)


