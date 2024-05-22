"""def find_missing(lst):
    max = lst[0]
    for i in lst:
      if i > max:
        max= i
    min = lst [0]
    for i in lst:
      if i < min:
        min = i
    missing = max+1
    list1=[]
    for _ in lst:
        max = max -1
        if max not in lst:
          list1.append(max)
    return list1

# Driver code
lst = [1,5,4,2,2, 2,2, 7,8, 10]
print(find_missing(lst)[::-1])
a=[[1,2,3],[4,15,6],[17,8,93]]
n=len(a)
b=0
c=0
for i in range(n):
    for j in range(n):
     if(i==j):
        b+=a[i][j]
     if((i+j)==(n-1)):
         c+=a[i][j]
if(b>c):
    print(b-c)
else:
    print(c-b)
def bcd_addition(bcd1, bcd2):
        # Pad the BCD strings with leading zeros to make them of the same length
    max_length = max(len(bcd1), len(bcd2))
    bcd1 = bcd1.zfill(max_length)
    bcd2 = bcd2.zfill(max_length)
    carry = 0
    result = []
    for i in range(max_length - 1, -1, -1):
        digit1 = int(bcd1[i])
        digit2 = int(bcd2[i])
        temp_sum = digit1 + digit2 + carry
        if temp_sum > 9:
            carry = 1
            temp_sum -= 10
        else:
            carry = 0
        result.insert(0, str(temp_sum))
    if carry:
        result.insert(0, str(carry))
    return ''.join(result)
# Example usage:
bcd_num1 = "1101"
bcd_num2 = "0110"
result =bcd_addition(bcd_num1, bcd_num2)
print("BCD Addition Result:", result)"""
def parde(inputBits):
    a=inputBits
    if len(a)%4!=0:
        print("Invalid Input ")
    else:
        lst=['0','1','2','3','4','5','6','7','8','9','+','-','=','/']
        print("13",lst[13])
        for i in range(0,len(a),+4):
            temp=a[i:i+4]
            btd=int(temp,2)
            print(btd)
    pass
parde(620)