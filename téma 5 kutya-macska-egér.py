# írj egy programot, amely kiírja a konzolba a számokat 1-től 100-ig. Ha a szám osztható 3-mal, írja mellé, hogy „kutya”. Ha a szám osztható 5-tel, írja mellé, hogy „cica”. Ha szám osztható 3-mal és 5-tel is, írja mellé, hogy „egér”.
# A programod a következő kritériumoknak feleljen meg:
#    Egy while ciklusból álljon.
#    A cikluson belül használj if, elif és else ágakat.
#    A feltételes utasításokon belül használd a print() függényt.

counter = 1
last_number = 100

while counter <= last_number:
    if counter % (3*5) == 0:
        print(str(counter) + 'egér')
    elif counter % 5 == 0:
        print(str(counter) + 'cica')
    elif counter % 3 == 0:
        print(str(counter) + 'kutya')
    else:
        print(str(counter))
    
    counter +=1

counter
    