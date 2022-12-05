#generate "-" with given number input

def linePrinter(num):
    result = []
    for i in range(num):
        result.append("-")
    print("".join(result))

linePrinter(5)
linePrinter(4)
linePrinter(3)
linePrinter(2)
linePrinter(1)