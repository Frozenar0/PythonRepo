def count_sheep(n):
    sentence = []
    for i in range(n):
        sentence.append(str(i+1))
        sentence.append(" sheep...")
    return "".join(sentence)

count_sheep(5)