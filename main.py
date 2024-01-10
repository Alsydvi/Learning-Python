if __name__ == "__main__":
   year = int(input("Give me a year and I will determine whether it is a leap year or not: "))
   print("You typed " + str(year))
   if type(year//4) == int:
       print("Leap year!")
   elif type(year//400) == int:
       print("Leap year!")
   else:
       print("Not a leap year :(")

