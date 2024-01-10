# Segítsé Hófehérkének nyilvántartani a törpéket. 
# Készíts egy számlálót, hogy melyik törpe, hol van éppen. 
# Nem minden törpe van a bányában, az 5-6-7. törpe még otthon alszik. 

number_of_dwarfs = 1
sum_of_dwarfs = 7
working_dwarfs = 4

while number_of_dwarfs <= working_dwarfs:
    print('A(z)' + str(number_of_dwarfs) + '. törpe a bányában dolgozik.')
    number_of_dwarfs +=1

while number_of_dwarfs <= sum_of_dwarfs:
    print('A(z)' + str(number_of_dwarfs) + '. törpe otthon alszik.')
    number_of_dwarfs +=1

number_of_dwarfs