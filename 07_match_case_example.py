#match...case is a cleaner way to check many conditions, like if...elif...else, and run code that matches.
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

output : wednesday

...................................................


day = "monday"
match day:

case "sunday":
     print("Holiday ahe")
case "monday":
    print"college ahe"
case "saturday":
    print("Half day ahe")
case_:
    print("Normal day")

#output: college ahe

