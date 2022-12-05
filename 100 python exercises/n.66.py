#check if a word is plural or singular

def pluralchecker(word):
    if word[-1] == "s":
        print("plural")
    else:
        print("singular")

pluralchecker("lemon")
pluralchecker("lemons")
pluralchecker("aristocracy")
pluralchecker("aristocracies")