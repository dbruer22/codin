import string
di=dict(zip(string.letters,[ord(c)%32 for c in string.letters]))
f = di['c']
print f
