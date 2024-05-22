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
print("Sorted Even Array:", evenArr)
oddArr = sorted(oddArr)
print("Sorted Odd Array:", oddArr[0:len(oddArr)])
print(evenArr[1] + oddArr[1])
evenArr = sorted(evenArr)
print("Sorted Even Array:", evenArr[0:len(evenArr)])
oddArr = sorted(oddArr)
print("Sorted Odd Array:", oddArr[0:len(oddArr)])
print(evenArr[1] + oddArr[1])