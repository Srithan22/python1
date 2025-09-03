def divi(n):
    if n%5==0 and n%11==0:
        return "divisible by 5,11";
    return "no"
print(divi(int(input("enter num"))))