import sys
try:
    print("hello my name is", sys.argv[1])
except:
    print("no name entered")
if len(sys.argv)>2:
    print("too many arguments")
elif len(sys.argv)<2:
    print("too less arguments")
else:
    print("hello my name is", sys.argv[1])
    
#nested loops
rows = int(input())
columns = int(input())
symbol = input()
for i in range(rows):
    for j in range(columns):
        print(symbol)
