def is_leap_year(year):
    if (year/4) == float(year//4):
       return "Leap year!"
    elif (year/400) == float(year//400):
       return "Leap year!"
    else:
       return "Not a leap year :("

if __name__ == "__main__":
   year = int(input("Give me a year and I will determine whether it is a leap year or not: "))

   print("You typed " + str(year))

   print(is_leap_year(year))



