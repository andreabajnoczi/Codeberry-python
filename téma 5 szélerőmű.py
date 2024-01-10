# Egy szélerőműfarm felkért rá, hogy építs nekik egy kontrolláló programot, amely a következőket tudja:
#    Adjon egy állapotjelentést minden egyes turbináról, és számítsa ki az adott turbina bekapcsolásának a pillanatában összesen termelt energiamennyiséget (pl. a 3. turbinánál számítsa ki az első 3 turbina által termelt összenergiát).
#    Összesen 25 szélturbinájuk van.
#    A mai napon az első 10 turbina teljes fordulaton üzemel, egyenként 2000 MWh-t termelve. A következő 10 turbina fél fordulaton üzemel, egyenként 1000 MWh-t termelve. Az utolsó 5 turbina jelenleg nem működik.
# programra vonatkozó kérések:
#    Listázza ki az első 10 turbinát a konzolba, a következő üzenettel: "A(z) X. számú szélturbina teljes fordulaton működik, 2000 MWh-t termelve. A farmon termelt összenergia jelenleg Y MWh."
#    Listázza ki a következő 10 turbinát a konzolba, a következő üzenettel: "A(z) X. számú szélturbina fél fordulaton működik, 1000 MWh-t termelve. A farmon termelt összenergia jelenleg Y MWh."
#    Listázza ki az utolsó 5 turbinát a konzolba, a következő üzenettel: "A(z) X. számú szélturbina nem működik, 0 MWh-t termelve. A farmon termelt összenergia jelenleg Y MWh."
#    A feladat megoldásához egyetlen while ciklust használj, és az üzenetekben változókat használj számok helyett.
#    Valószínűleg szükséged lesz egy all_turbines, egy turbine_power, egy sum_powerés egy turbine_counter változóra a programban.

counter = 1
power_counter = 0
sum_turbine = 25
whole_power_turbine = 10
whole_power = 2000
half_power_turbine  =10+10
half_power = 2000/2

while counter <= sum_turbine:
    if counter <= whole_power_turbine:
        power_counter +=whole_power
        print('A(z) ' +  str(counter) + '. számú szélturbina teljes fordulaton működik, 2000 MWh-t termelve. A farmon termelt összenergia jelenleg ' + str(power_counter) + ' MWh.')
        counter +=1
    elif counter <= half_power_turbine:
        power_counter +=half_power
        print('A(z) ' +  str(counter) + '. számú szélturbina fél fordulaton működik, 1000 MWh-t termelve. A farmon termelt összenergia jelenleg ' + str(power_counter) + ' MWh.')
        counter +=1
    else:
        print('A(z) ' + str(counter) + '. számú szélturbina nem működik, 0 MWh-t termelve. A farmon termelt összenergia jelenleg ' + str(power_counter) + ' MWh.')
        counter +=1

counter

