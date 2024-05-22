def calculate (r, unit, arr, n):
    if n == 0:
        return -1
    totalFoodRequired = r * unit
    foodTillNow = 0
    house = 0

    for house in range (n):
        foodTillNow += arr[house]
        if foodTillNow>=totalFoodRequired:
            break
    if totalFoodRequired > foodTillNow:
        return 0
    return house + 1

r = int (input ("Enter no. of rats"))
unit = int (input ("Enter no. of units"))
n = int (input ("Enter a number "))
arr = list (map (int, input ().split ()))
print (calculate (r, unit, arr, n))

arr=list()
for i in range(5):
    i=int(input())
    arr.append(i)
print(arr)
"""
def OperationsBinaryString(str):
    a=int(str[0])
    i=1
    while i< len(str):
        if str[i]=='A':
            a&=int(str[i+1])
        elif str[i]=='B':
            a|=int(str[i+1])
        else:
            a^=int(str[i+1])
        i+=2
    return a
str=input()
print(OperationsBinaryString(str))"""
def findCount(n, arr, num, diff):
    count=0
    for i in range(n):
        if(abs(arr[i]-num)<=diff):
            count+=1

    if count:
        return count
    return 0
arr=list(map(int,input().split()))
n=len(arr)
num=int(input())
diff=int(input())
print(findCount(n, arr, num, diff))
n = int(input())
sum1 = int(input())
arr = list(map(int, input().split()))
if n < 2:
    print('-1')
arr = sorted(arr)
for i in range(n-1):
    if arr[i] + arr[i+1] < sum1:
        print(arr[i] * arr[i+1])
        break
else:
    print('0')
array = []
evenArr = []
oddArr = []
n = int(input("Enter the size of the array:"))
for i in range(0,n):
    number = int(input("Enter Element at {} index:".format(i)))
    array.append(number)
    if i % 2 == 0:
        evenArr.append(array[i])
    else:
        oddArr.append(array[i])
evenArr = sorted(evenArr)
print("Sorted Even Array:", evenArr[0:len(evenArr)])
oddArr = sorted(oddArr)
print("Sorted Odd Array:", oddArr[0:len(oddArr)])
print(evenArr[1] + oddArr[1])
evenArr = sorted(evenArr)
print("Sorted Even Array:", evenArr[0:len(evenArr)])
oddArr = sorted(oddArr)
print("Sorted Odd Array:", oddArr[0:len(oddArr)])
print(evenArr[1] + oddArr[1])

first_number = int(input())
second_number = int(input())
for i in range(first_number, second_number+1):
    reverse = 0
    temp = i
while temp != 0:
    remainder = temp % 10
    reverse = (reverse * 10)+remainder
    temp = temp // 10
    if i == reverse:
        pass
print(reverse)