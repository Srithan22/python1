def days():
    n=int(input("Enter days to covert into years,months,days "))
    min=n%365
    left=n-min
    mon=min%30
    print("Remaining years {}".format(left//365))
    print("months {}".format(min//30))
    print("days {}".format(mon))
days()