#write a program to check wheter a given character is vowel or consonant

def VowCons(char):
    if char.lower() == "a" \
            or char.lower() == "a" \
            or char.lower() == "e" \
            or char.lower() == "i"\
            or char.lower() == "o"\
            or char.lower() == "u":
        print(char, "is a vowel")
    else:
        print(char, "is a consonant")


VowCons("a")
VowCons("b")
VowCons("c")
VowCons("d")
VowCons("e")
