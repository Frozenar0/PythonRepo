def disemvowel(string_):
    vowels = ["u", "e", "i", "o", "a","A","E","I","O","U"]
    string_ = [*string_]
    print("done")
    for i in string_:
        if i.lower() in vowels:
            string_.remove(i)
    if any(item in string_ for item in vowels):
        return disemvowel(string_)
    else:
        return "".join(string_)



print(disemvowel(' W +wDe{zh#yq&M>Ue* go.JlN ^E OeR;So^eO#mEH?Ye`|soAkUwW eA&t \\X YADi@?Eq . O*>H'))