a = 2**1000
b = str(a)
c = []

for digit in b:
    c.append (int(digit))

answer = sum(c)
print (answer)
