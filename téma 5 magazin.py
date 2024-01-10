# FEALADAT 1
# írj egy programot az online magazinnak: értesítsd a látogatókat, hogy megtekinthetik-e a tartalmat.
# A programod a következő kritériumoknak feleljen meg:
#    Mentsd el a látogató életkorát egy age nevű változóba. Az értékét a input()függvénnyel add meg, a következő kérdéssel elkérve a látogató életkorát: Hány éves vagy?.
#    Ne felejtsd el használni az int() függvényt.
#    Ha a látogató 18 évesnél fiatalabb, a konzol írja ki ezt: "Sajnáljuk, de ez a cikk csak 18 éven felüliek számára érhető el.".
#    Ha a látogató legalább 18 éves,, a konzol a következőt írja ki: "Köszönjük! Elolvashatod ezt a cikket.".
#    Ha a látogató éppen 18 éves, a konzol a következőt írja ki: "Pont 18? Gratulálunk, üdv a felnőttek között! Jó szórakozást a cikkhez!".

age = int(input('Hány éves vagy? '))

if age < 18:
    print('Sajnáljuk, de ez a cikk csak 18 éven felüliek számára érhető el.')
elif age == 18:
    print('Pont 18? Gratulálunk, üdv a felnőttek között! Jó szórakozást a cikkhez!')
else:
    print('Köszönjük! Elolvashatod a cikket.')

age