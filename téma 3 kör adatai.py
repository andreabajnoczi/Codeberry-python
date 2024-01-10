# FELADAT 4
# írj egy programot, amely kiszámolja egy tetszőleges kör kerületét és területét a kör sugara alapján.
# A programod a következő kritériumoknak feleljen meg:
#    Álljon három függvényből:
#        egy számolja ki a kör kerületét,
#        egy a területét,
#        egy pedig kérje be a sugarat a felhasználótól, majd a számítások után nyomtassa ki az eredményt a konzolba.

def circle_circumference(radius):
    return 2*radius*3.14

def circle_area(radius):
    return radius*radius*3.14

def print_circle_datas(radius_from_user):
    print('A kör kerülete: ' + str(circle_circumference(radius_from_user)) + ' méter.')
    print('A kör területe: ' + str(circle_area(radius_from_user)) + ' négyzetméter.')

print_circle_datas(4)
print_circle_datas(22)
print_circle_datas(3)
print_circle_datas(334)
