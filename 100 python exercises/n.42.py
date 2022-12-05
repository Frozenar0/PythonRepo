#turn a string into an integer

def egg(str):
    try:
        print(int(str))
    except:
        print("this string is not a number")


egg("12341")
egg("hello")
egg(123)