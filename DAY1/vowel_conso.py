def alpha(n):
    s='aeiou'
    if n in s:
        return " vowel"
    return "consonent"
print(alpha((input("enter alphabet "))))