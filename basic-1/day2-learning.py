'''name = input("enter your hame : ")
print("hello", name, "have a nice day")
#this is a comment 
"""this is a multi line comment 
it goes on for multiple lines on and on"""
#pseudo code is basically code given as command 
''''''it is basically algorythm given in a comment or 
its a given todo list split into bitesized comments
''''''
#named paramaters 
name1 = str(input("enter your name : "))
''''''when you wanna change the seperations in a print file u do , sep = ''
if u wanna change what the print statement ends with you do , end = ''
entering anything between those semicolens will print what it does after the print statement is done
''''''
print("hello world i like cheese", sep = '-', end = '000')
#string functions 
name = name.strip()#removes blank spaces
name = name.upper()#makes all uppercase
name = name.lower()#makes all lowercase
name = name.capitalize()#it just makes first letter capital
#split name into two parts
namefirst, namelast = name.split(" ")'''
x = int(input('enter first number : '))
y = int(input('enter second number : '))
z = x + y
print(z)
#if you dont typecast as int or float n stuff it goes as string and gets concatinated
k = float(input('enter a float'))
k = round(k, 10)#this is for rounding off numbers
#to automatically include comma we do this ->
print(f"{k:,}")
#inventing functions are coolll
def hello(name = 'gabe'):
    print(f"hello {name}")
#return value stuff

def main():
    x = int(input("what is x : "))
    print("x squared is : ", square(x))
def square(n):
    return n*n
main()