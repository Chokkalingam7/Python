a=int(input("Enter first number"))
b=int(input("Enter the second number"))
while(a!=b):
    if(a>b):
        a=a-b
    else:
        b=b-a
print(a)def proper_compression(s):
    compressed_str = []

    i = 0
    while i < len(s):
        c = s[i]
        count = int(s[i + 1])
        while count > 0:
            compressed_str.append(c)
            count -= 1
        i += 2


    return ''.join(compressed_str)

# Example usage:
input_str = "a3b5c2a2"
compressed_result = proper_compression(input_str)
print(compressed_result)  # Output: "aaabbbbbcc"
# Input: Decimal number
decimal_number = int(input("Enter a decimal number: "))

# Using the bin() function to convert to binary
binary_representation = bin(decimal_number)

# Printing the binary representation
print(f"The binary representation of {decimal_number} is: {binary_representation[2:]}")

m=int(input("enter the number "))
i=0
j=1
print("The Fibonacci Series ",i)
for a in range(m+1):
    print(j,end=" ")
    sum=i+j
    i=j
    j=sum
