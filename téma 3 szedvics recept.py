# FELADAT
# A programod a következő kritériumoknak feleljen meg:
#    Egy darab függvényből álljon.
#    A függvény neve legyen print_sandwich_recipe().
#    A függvény nyomtassa ki a konzolba a következő utasításlistát:
#
#    Fogj két szelet kenyeret.
#    Az egyik szeletre nyomj szósz-t.
#    Helyezz a kenyérre két szelet hús-t.
#    Rakj rá egy szelet sajt-ot.
#    Koronázd meg pár szelet/karika/csipet ilyen zöldséggel: zöldség.
#    Borítsd be a szendvicset a másik szelet kenyérrel.
#    Jó étvágyat!
#
#    A 2., 3., 4. és 5. sorban a jelölt helyekre a függvény helyettesítse be a megfelelő hozzávalókat.
#    Az adat érkezzen a függvény paramétereiből.
#    A paraméterek feleljenek meg az elnevezési szabályoknak és konvencióknak.
#    Hívd meg a függvényt.

def print_sandwich_recipe(sauce, meat, cheese, vegetable):
    print('Fogj két szelet kenyeret.')
    print('Az egyik szeletre nyomj ' + sauce + 't.')
    print('Helyezz a kenyérre két szelet ' + meat + 't.')
    print('Rakj rá egy szelet ' + cheese + 't.')
    print('Koronázd meg pár szelet/karika/csipet ilyen zöldséggel: '  + vegetable + '.')
    print('Borítsd be a szendvicset a másik szelet kenyérrel.')
    print('Jó étvágyat!')

print_sandwich_recipe('majonéz', 'téliszalámi', 'edami', 'paradicsom')

def print_sandwich_recipe_2(sauce, meat, cheese, vegetable):
    print('Fogj két szelet kenyeret.')
    print('Az egyik szeletre nyomj '  + sauce + 't.')
    print('Helyezz a kenyérre két szelet ' + meat + 't.')
    print('Rakj rá egy szelet '  + cheese + 't.')
    print('Koronázd meg pár szelet/karika/csipet ilyen zöldséggel: '  + vegetable + '.')
    print('Borítsd be a szendvicset a másik szelet kenyérrel.')
    print('Jó étvágyat!')

print_sandwich_recipe_2('majonéz', 'téliszalámi', 'tilsiter', 'paprika')