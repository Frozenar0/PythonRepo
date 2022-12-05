#check if a string is a palindrome


def palindrome(string):
    print(string.replace(" ", ""))
    print((string[::-1]).replace(" ", ""))
    if (string[::-1]).replace(" ", "") == string.replace(" ", ""):

        print("it's a palindrome")
    else:
        print("not a palindrome")

palindrome("no lemon, no melon")