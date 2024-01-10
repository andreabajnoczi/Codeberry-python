#Egy online kereskedő áruház szeretné nyílvántartani a vásárlóik által megadott bankkártyák kibocsátóit. A te feladatod lesz elkészíteni azt a funkciót, ami megmondja az áruháznak, hogy egy kártya melyik bankhoz tartozik.
#A függvényednek a következő feladatot kell ellátnia:
#    Bejövő paraméterként kap egy bankkártyaszámot string formájában.
#    Megvizsgálja a kártyaszám első négy karakterét az alábbiak alapján:
#       Ha az első négy karakter az 1234, akkor a következőt írja ki a konzolra: A kártyaszám számú kártya a Gringotts Varázslóbank tulajdona.
#        Ha az első négy karakter a 9876, akkor a következőt írja ki a konzolra: A kártyaszám számú kártya a Galaktikus Birodalom kizárólagos tulajdona.
#        Ha az első négy karakter a 4567, akkor a következőt írja ki a konzolra: A kártyaszám számú kártya Dagobert bácsi széfjének tulajdonát képezi.

card_of_skywalker = '9876435623789761'
card_of_dobby = '1234567812345678'
card_of_donald = '456789123456'

def check_the_bankcard(card_number):
    if card_number[0:4] == '1234':
        print('A ' + card_number +  'számú kártya a Gringotts Varázslóbank tulajdona.')
    elif card_number[0:4] == '9876':
        print('A ' + card_number + ' számú kártya a Galaktikus Birodalom kizárólagos tulajdona.')
    elif card_number[0:4] == '4567':
        print('A ' + card_number + ' számú kártya Dagobert bácsi széfjének tulajdonát képezi.')
        
check_the_bankcard(card_of_dobby)
check_the_bankcard(card_of_donald)
check_the_bankcard(card_of_skywalker)

