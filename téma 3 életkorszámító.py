# FELADAT 3
#készíts egy életkor-kalkulátort!
# A programod a következő kritériumoknak feleljen meg:
#
#   Egy darab függvényből és egy print() utasításból álljon.
#    A függvény neve legyen calculate_age().
#    A függvény fogadjon be két paramétert:
#        A jelenlegi évet.
#        A felhasználó születési évét.
#    A paraméterek legyenek a szabályoknak és konvencióknak megfelelően elnevezve.
#    A függvény számolja ki a paraméterekből a felhasználó korát, és mentse el egy age nevű változóban.
#    Az age változót adja vissza a függvény, mint return value-t.
#    A függvény után egy print() utasítás nyomtassa ki a konzolba a te életkorodat úgy, hogy a calculate_age() függvényt hívod meg magában a print()-ben.


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
    
print('A felhasználó életkora ' + str(calculate_age(2023, 1981)) + ' év.')

