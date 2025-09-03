a=int(input("enter customer num "))
b=(input("enter Name "))
m1=int(input("enter present month reading "))
m2=int(input("enter last month reading "))
u=m1-m2
avg=u*3.8
print("Name {}".format(b))
print("customer num {}".format(a))
print("total units{}".format(u))
print(f"curr bill {avg}")

