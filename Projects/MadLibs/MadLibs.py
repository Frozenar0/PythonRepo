class CreateMadLib:
    def __init__(self, text, words):
        self.text = text
        self.words = words


madLib = CreateMadLib(["Today I went to my favorite Taco Stand called the", "",
                       ".Unlike most food stands, they cook and prepare the food in a", "while you",
                       ".The best thing on the menu is the ",
                       ".Instead of ground beef they fill the taco with ",
                       "cheese, and top it off with a salsa made from ",
                       ".If that doesn't make your mouth water, then it is just like ",
                       " always says:", "!"
                       ],
                      ["An Adjective", "Some foods", "A Verb", "A Saying", "A Noun", "Some other Foods", "A Color",
                       "Something you would ride in", "An Animal", "A Person",
                       ])
# creates the dictionary of word categories(keys) and empty spaces for now(values)
empties = dict.fromkeys(madLib.words, "empty")



# fills the dictionary with user choices
def askinput():
    for k, v in empties.items():
        empties[k] = input("please insert " + k + "> ")


# creates a list of alternating elements from madLib.text and the values of empties
def countlist(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
            for sub in [lst1, lst2]]


# Driver code
def main():
    askinput()
    composition = countlist(madLib.text, list(empties.values()))
    print(" ".join(composition))


main()


# CEMETERY
# def Com
# position():
#     composed = []
#
#     for sentence in madLib.text:
#         if sentence not in composed:
#             composed.append(sentence)
#             for k, v in empties.items():
#                 if v not in composed:
#                     composed.append(v)
#                 continue
#         continue
#
#
#
#
#     print(composed)
#
# askInput()
# Composition()


# libs = "Today I went to my favorite Taco Stand called the " + empties["word0"] + " " + empties[
#             'word1'] + ". Unlike most food stands, they cook and prepare the food in a " + empties[
#                    'word2'] + " while you " + empties['word3'] + ". The best thing on the menu is the " + empties[
#                    'word4'] + " " + empties['word5'] + ". Instead of ground beef they fill the taco with " + empties[
#                    'word6'] + " cheese, and top it off with a salsa made from " + empties[
#                    'word7'] + ". If that doesn't make your mouth water, then it is just like " + empties[
#                    'word8'] + " always says: " + empties['word9'] + "!"
#
# print(empties)
# print(libs)


# empties = {
#       TacoLib.word0: "empty",
#       "word1": "empty",
#       "word2": "empty",
#       "word3": "empty",
#       "word4": "empty",
#       "word5": "empty",
#       "word6": "empty",
#       "word7": "empty",
#       "word8": "empty",
#       "word9": "empty"
# }
#
# print(empties[TacoLib.word0])
