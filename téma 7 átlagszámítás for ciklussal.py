# Az egyik probléma, amit a FOR ciklus segítségével könnyen meg tudunk oldani, az ÁTLAGSZÁMÍTÁS.

# írj két függvényt:
#    sum_of_scores()
#        Kap egy listát paraméterként
#        Kiszámolja a lista elemeinek összegét
#        Visszaadja az összeg értékét
#    calculate_average()
#        Kap egy listát és egy összeget paraméterként
#        Kiszámolja a lista elemeinek átlagát
#        Visszaadja az átlag értékét

scores_this_season = [116, 124, 115, 102, 111, 106, 99, 90]

def sum_of_scores(list):
    sum = 0
    for element in list:
        sum += element
    return sum

def calculate_average(list, sum):
    average = sum / len(list)
    return average

print(calculate_average(scores_this_season, sum_of_scores(scores_this_season)))

