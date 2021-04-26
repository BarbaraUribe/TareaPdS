import re

print("Ingresar cadena de caracteres: \n")
s = ""
s = input()
l = list(s)
sf = ""
lf = list()

if len(l) == 0:
    print("Error, ingresó una cadena de caracteres vacía")

if len(l) == 1:
    print(s)

c = ""
a = 0
g = 0

for i in l:
    if i != c:
        m = re.match("^[0-9]$", i)
        lf.append(c)
        lf.append(a)
        if m:
            lf.append("-")
            g += 1
        c = i
        a = 1
    else:
        a += 1

lf.append(c)
lf.append(a)

for i in lf:
    sf += str(i)

if len(s) <= len(sf)-1-g:
    print(s)
else:
    print(sf[1:])