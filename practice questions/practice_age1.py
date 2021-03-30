def calc_age(age):
    return age * 365
print(calc_age(21))

def find_perimeter(length, width):
    perimiter = (length*2)+(width*2)
    return perimiter

def time_for_milk_and_cookies(month, day):
    if month == 12 and day == 24:
        return True
    else:
        return False

def sum_polygon(n):
    angle = (n - 2) * 180
    return angle