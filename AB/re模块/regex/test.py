import re 

f = open('regex')
l = []
pattern = r'[A-Z][_.0-9a-zA-Z]*'

for line in f:
    l += re.findall(pattern,line)

print(l)
