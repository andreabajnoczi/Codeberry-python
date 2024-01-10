# FELADAT 1
# írj egy kis visszaszámláló programot. A program 10-től 0-ig számolja vissza a másodperceket, a hátramaradó időt a következőképpen kiírva a konzolba: „X másodperc a kilövésig.”
# A programod a következő kritériumoknak feleljen meg:
#    Szerepel benne egy while ciklus.
#    Szerepel benne egy seconds nevű változó, amely a fennmaradó időt tárolja el.
#    A seconds változót használja a ciklus kontrollálására.
#    A fennmaradó időt minden iteráció során kiírja a konzolba.

seconds = 10

while seconds>0:
    print(str(seconds) + ' másodperc a kilövésig.')
    seconds -=1

if seconds == 0:
    print('KILÖVÉS')

seconds