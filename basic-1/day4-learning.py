#match is a switch
name = str(input("whats your name : "))
match name:
    case "harry" | "hermione" | "ron":
        print("griffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who?")
#loops is basically a code that is repeated over and over again 
'''ideally through a flowchat you can go through things one by one
but it is more tedious and more ram consuming to have more lines that
do the same thing rather than have one set of code that repeats a certian 
number of times using a loop
'''
#while loop
i = 0
while i < 3:
    print("meow")
    i+=1
for i in range(1, 10):
    print("chingchong")
while True:
    n = int(input("what is the value of n "))
    if n<0:
        continue
    else:
        break
def main():
    number = getnumber()
    meow(10)
def getnumber():
    while True:
        n = int(input())
        if n>0:
            return n
def meow(n):
    for i in range(n):
        print("meow")
#list is a bunch of variables stored in one big varible can be non homogeneous
students = ['chigga', 'gigga', 'diga']
''' a list can be iterated by using an index, indexing is 
the order in which it is ordered and it begins count with 0'''
#dictionary using curly braces, 
students = {'chigga':100, 'digga':200}
