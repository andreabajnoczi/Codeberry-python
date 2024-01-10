# írj egy olyan programot, amely percenként elszámol a meccs végéig, és kinyomtatja minden percben az aktuális negyedet és percet. Az elkészítéshez két for ciklust kell használnod:
#    Az első ciklus minden negyed elején írja ki, hogy hányadik negyedben járunk, pl: 1. negyed.
#    A második ciklus minden percben írja ki, hogy éppen mikor járunk: 1. negyed, 1. perc.
#    Négy negyed van, negyedenként tizenkét perccel.

quarters = 4
minutes = 12

def timer():
    for quarter in range (1, quarters+1):
        print(str(quarter) + '. negyed: ')
        for minute in range (1, minutes+1):
            print(str(quarter) + '. negyed, ' + str(minute) + '. perc' )

timer()
