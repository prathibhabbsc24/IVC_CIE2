n = int(input("Enter number: "))
temp = n
s = 0

while temp > 0:
    digit = temp % 10
    s += digit
    temp //= 10

if str(s) == str(s)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
    
    

    
    