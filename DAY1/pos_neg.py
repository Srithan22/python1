def pos_neg(n):
    if n>0:
        return "positive";
    else: 
      if n<0:
        return "negative"
    return "zero"
print(pos_neg(int(input("enter num "))))