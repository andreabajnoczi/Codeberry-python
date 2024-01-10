# FELADAT 2
# Azt szeretnénk, ha lenne egy while ciklusunk, amely kilistázza a számokat 1-től 20-ig, és eldönti róluk, hogy párosak-e vagy páratlanok.
# Amikor a ciklus eléri a 10-et, akkor a következő mondatot írja ki a konzolba: A 10 a legszebb páros szám.

counter = 1
last_number = 20

while counter <= last_number:
    if counter == 10:
        print(str(counter) + ' a legszebb szám.')
    elif counter % 2 == 0:
        print(str(counter) + ' páros szám.')
    else:
        print(str(counter) + ' páratlan szám.')
    counter +=1

counter