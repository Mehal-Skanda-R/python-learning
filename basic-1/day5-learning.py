#dictionary
''' dict youc an asign a key to a value its basically a 
two dimentional thing, you can assign like word and meaning 
or name and roll number together 
'''
students = {'hermione':'gryffindor',
            'harry':'gryffindor',
            'ron':'gryffindor',
            'draco':'slytherin'}
'''
print('#')
print('#')
print('#')
n = int(input("enter value of n "))
for i in range(n):
    print("#")
def main():
    n = int(input("enter value of n:"))
    printcolumn(n)
def printcolumn(n):
    for i in range(n):
        print("#")

'''
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, end ='')
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

result = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                result.append([i, j, k])

print(result)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    highest = max(arr)

    while highest in arr:
        arr.remove(highest)

    print(max(arr))
if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = []

    for student in students:
        if student[1] not in scores:
            scores.append(student[1])

    scores.sort()
    second_lowest = scores[1]

    names = []

    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    names.sort()

    for name in names:
        print(name)
   