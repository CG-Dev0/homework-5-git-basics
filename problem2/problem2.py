def date_format(my_string: str):
    year = my_string[-4:]
    month = my_string[:2]
    day = my_string[3:5]
    return f"{year}-{month}-{day}"

#print(date_format('MM/DD/YYYY'))