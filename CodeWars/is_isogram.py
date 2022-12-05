def is_isogram(string):
    string = string.lower()
    if len(string) <= 0:
        return True
    else:
        for i in [*string]:
            print(i)
            if string.count(i) > 1:
                return False
                break
        return True


print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))