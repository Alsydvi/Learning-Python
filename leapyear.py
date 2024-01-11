def is_leap_year_ad_num(year):
    year = int(year.upper().replace("AD", ""))
    if ((int(year))/4) == float(year//4):
       return "Leap year!"
    elif ((int(year))/400) == float(year//400):
       return "Leap year!"
    else:
       return "Not a leap year :("

def is_leap_year_bc_num(year):
    year = int(year.upper().replace("BC", ""))
    if ((year-1)/4) == float((year-1)//4):
        return "Leap year!"
    elif ((year-1)/400) == float((year-1)//400):
        return "Leap year!"
    else:
        return "Not a leap year :("


if __name__ == "__main__":
   year = input("Give me a year with numbers and I will determine whether it is a leap year or not, you may add 'BC' for bc years. : ")


if year.isdigit() or "AD" in year.upper():
        print(is_leap_year_ad_num((year)))

if "BC" in year.upper():
        print(is_leap_year_bc_num((year)))

print("You typed " + str(year))




