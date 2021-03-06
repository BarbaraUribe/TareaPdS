import re
import logging
import datetime

logging.basicConfig(
    filename=datetime.datetime.now().strftime("%d") + "-" + datetime.datetime.now().strftime("%m") + "-" +
             datetime.datetime.now().strftime("%Y") + ".log", level=logging.DEBUG)
print("Ingresar cadena de caracteres: \n")
s = input()
l = list(s)
sf = ""
lf = list()


def check(s, l, sf, lf):

    x = re.search("-+", s)

    if x:
        logging.error(datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M") + ":"
                     + datetime.datetime.now().strftime("%S") + " \"" + s + "\"" +
                     ". Error: ingresó el caracter \"-\" que no está permitido ")
        print("Error: ingresó el caracter \"-\" que no está permitido.")
        return 1

    if len(l) == 0:
        logging.error(datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M") + ":"
                     + datetime.datetime.now().strftime("%S") + " \"" + s + "\"" +
                     ". Error: ingresó una cadena de caracteres vacía")
        print("Error: ingresó una cadena de caracteres vacía.")
        return 1

    if len(l) == 1:
        print(s)
        return 0

    if len(l) > 50:
        logging.error(datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M") + ":"
                      + datetime.datetime.now().strftime("%S") + " \"" + s + "\"" +
                      ". Error: ingresó una cadena de caracteres muy larga")
        print("Error: ingresó una cadena de caracteres muy larga.")
        return 1
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

    if len(s) <= len(sf) - 1 - g:
        logging.info(datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M") + ":"
                     + datetime.datetime.now().strftime("%S") + " \"" + s + "\", \"" + s + "\"")
        print(s)
        return 0
    else:
        logging.info(datetime.datetime.now().strftime("%H") + ":" + datetime.datetime.now().strftime("%M") + ":"
                     + datetime.datetime.now().strftime("%S") + " \"" + s + "\", " + "\"" + sf[1:] + "\"")
        print(sf[1:])
        return 0


check(s, l, sf, lf)
