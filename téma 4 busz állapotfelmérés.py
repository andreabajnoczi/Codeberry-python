# FELADAT 3
#Képzeld el, hogy egy városi buszjáratokat üzemeltető céget vezetsz. A vezető gépész minden reggel megvizsgálja a garázsban álló autóbuszokat. Szeretnéd, ha egy alkalmazásban rögzítené a buszok összdarabszámát és az üzemképes buszok számát.
# A programod a következő kritériumoknak feleljen meg:
#    Két while ciklust használ.
#    Szerepel benne egy total_buses változó, amely a buszok összdarabszámát tárolja.
#    Szerepel benne egy working_buses változó, amely az üzemképes buszok számát tárolja.
#    Szerepel benne egy bus_counter változó, amely az aktuális busz sorszámát tárolja.
#    Az első ciklus az üzemképes buszokra vonatkozó üzeneteket írja ki, a második ciklus pedig az üzemen kívüli buszokra vonatkozó üzeneteket.
#    Az aktuális busz sorszáma a bus_counter változóból származzon.
#    Úgy írd meg a programot, hogy az akkor is helyesen fusson le, ha megváltozik a buszok összdarabszáma és/vagy az üzemképes buszok darabszáma.


bus_counter = 1
total_buses = 12
working_buses = 8

while bus_counter <= working_buses:
    print('A(z)' + str(bus_counter) + '. számú busz üzemképes, sofőrre vár.')
    bus_counter += 1

while bus_counter <= total_buses:
    print('A(z)' + str(bus_counter) + '. számú busz üzemen kívül van, szerelőre vár.')
    bus_counter +=1

bus_counter