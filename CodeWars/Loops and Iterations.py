#iteration variable
def blastoff(n):
    while n > 0 :
        print(n)
        n = n - 1
    print("blastoff!")
    print(n)

#badly constructed iteration variable
def badLoop():
    n = 5
    while n > 0:
        print("lather")
        print("rinse")
    print("dry off")


#another loop, zero trip loop as it doesn't run
def anotherLoop():
    while n > 0 :
        print("lather")
        print("rinse")
    print("dry off")


#breaking out of a loop
def breakLoop():
    while True:
        line = input('> ')
        if line =="done" :
            break
        print(line)
    print('done')


#skipping loop blocks with continue
def skipLoop():
    while True:
        line = input('>' )
        if line[0] =='#':
            continue
        if line == "done":
            break
        print(line)
    print('done')

#definite loop
for i in [5,4,3,2,1]:
    print(i)

skipLoop()