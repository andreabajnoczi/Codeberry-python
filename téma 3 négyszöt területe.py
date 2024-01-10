# FELADAT 2
#A kódodnak a következő kritériumoknak kell megfelelnie:
#    A függvény neve legyen calculate_rectangle_area().
#    Fogadjon be egy width (szélesség) és height (magasság) paramétert.
#    Számolja ki a megadott adatok alapján a négyszög területét.
#    Nyomtassa ki az eredményt a konzolba az alábbi stringben: 'A négyszög területe x négyzetméter.' 
#    (az x helyén a számítás eredményével).

def calculate_rectangle_area(width, height):
    area = width * height
    print('A négyszög területe: ' + str(area) + ' négyzetméter.')

calculate_rectangle_area(6, 3)

def calculate_rectangle_area_2(width, height):
    return width * height

print('A négyszög területe: ' + str(calculate_rectangle_area_2(5,2)) + ' négyzetméter.')

# DRY-kódja ugyanennek:

def calculate_rectangle_area_3(width, height):
    return width * height

def print_calculate_rectanle_area_3(width_from_user, height_from_user):
    area = calculate_rectangle_area_3(width_from_user, height_from_user)
    print('A négyszög területe: ' + str(area) + ' négyzetméter.')

print_calculate_rectanle_area_3(6,5)
      