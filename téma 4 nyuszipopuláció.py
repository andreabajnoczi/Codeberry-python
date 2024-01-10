# FELADAT 2 
#  Írj egy kis programot, amely a képzeletbeli Skylark-völgy nyúlpopulációjának a változását követi egy éven keresztül.
#    Az első hónap elején a kezdőpopuláció 30 nyusziból áll.
#    Az első hat hónap során minden hónap végére megduplázódik a populáció, ezt követően pedig minden hónapban megháromszorozódik.
# Írasd ki a konzolba ezeket a változásokat minden hónapra, a következő szöveggel: „A Skylark-völgy nyulainak száma X a(z) Y. hónap végén.”
# A programod a következő kritériumoknak feleljen meg:
#    Két while ciklusból áll.
#    Szerepel benne egy month_counter változó, amely a hónapok számát tárolja, valamint egy rabbit_population változó, amely a nyuszik számát tárolja.
#    A month_counter változó kontrollálja a ciklusokat.
#    A program minden iteráció során írjon ki a konzolba egy üzenetet, amely megmondja, hogy az aktuális hónap végén mi a nyuszik száma.
#    A program álljon le a 12. hónap végén.


rabbit_population = 30
month_counter = 1
sum_of_months = 12
half_time = 6

while month_counter <= half_time:
    rabbit_population *=2
    print('A Skylark-völgy nyulainak száma ' + str(rabbit_population) + ' a(z) ' + str(month_counter) + ' végén.')
    month_counter +=1

while month_counter <= sum_of_months:
    rabbit_population *=3
    print('A Skylark-völgy nyulainak száma ' + str(rabbit_population) + ' a(z) ' + str(month_counter) + ' végén.')
    month_counter +=1

rabbit_population           # vagy month_counter