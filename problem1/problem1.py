def is_leap_year(my_int: int):
    if my_int % 4 == 0 and my_int % 100 != 0 or my_int % 400 == 0 and my_int % 100 == 0:
        return True
    else:
        return False

#print(is_leap_year(2024))
#print(is_leap_year(2100))
#print(is_leap_year(2400))