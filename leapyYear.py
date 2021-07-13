def checkLeapYear(a):
    a = int(a)
    if ((a%400==0) or (a%4==0 and a%100!=0)):
        print(f"The year {a} is a leap year!")
    else:
        print(f"The year {a} is not a leap year!")
  
check = True

while check:
    try:
        year = int(input("Input a year to check if it's a leap year: "))
        checkLeapYear(year)
    except ValueError:
        print("Please enter a year!")
    cont = str.lower(input("Would you like to enter a new year?(y/n) "))
    if (cont != "y" and cont!='yes'):
            check = False
            print("Exiting")
