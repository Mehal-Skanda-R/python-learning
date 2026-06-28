print("hello")
#if and else if statements (elif)
x = int(input())
y = int(input())
'''if x == y:
    print("equal")
elif x>=y:
    print("greater")
else:
    print("lesser")'''
#this is called a controll flow, else is the ending statement. 
#or statements 
if x<y or x>y:
    print("not equal")
elif x!= y:
    print("chigga")
else:
    print("equal")
#using or statement is like logically or or logically and
'''its like saying if this and this is true then do this
else if this is true or this true then do this statement 
and then at the end if neither is true follow the else statement and solve
thats how or and and else if and else work 
'''
# % is remainder operator so it returns operator after division 
#off and even functions 
def main():
    x = int(input())
    if is_even(x):
        print("even")
    else:
        print("odd")
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
main()
