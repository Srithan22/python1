p=int(input("Enter principle"))
t=int(input("Enter  month"))
r=int(input("Enter intrest rate"))
si=(p*t*r)//100
in_hand=p+si
print("simple intrest {}".format(si))
print("total in hand {}".format(in_hand))