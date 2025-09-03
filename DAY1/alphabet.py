def alpha(n):
    s='qwertyuioplkjhgfdsazxcvbnm'
    if n in s:
        return "yes"
    return "no"
print(alpha((input("enter alphabet "))))