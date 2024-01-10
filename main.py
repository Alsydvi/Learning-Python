def is_leap_year_ad_num(year):
    if (year/4) == float(year//4):
       return "Leap year!"
    elif (year/400) == float(year//400):
       return "Leap year!"
    else:
       return "Not a leap year :("

def is_leap_year_bc_num(year):
    if (year/4)-1 == float(year//4)-1:


if __name__ == "__main__":
   year = input("Give me a year and I will determine whether it is a leap year or not: ")


    if year.isdigit() or "AD" in year.upper():
        print(is_leap_year_ad_num(int(year)))
    else:
        print(is_leap_year_bc_num(year))

   print("You typed " + str(year))




