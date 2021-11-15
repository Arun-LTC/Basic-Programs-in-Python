n=int(input("Input: "))
temp=n
s=0
while(n!=0):
    d=n%10
    s=d+s*10
    n=n//10
if(s == temp):
    print("{}: Palindrome".format(temp))
else:
    print("{}: Not a Palindrome".format(temp))
