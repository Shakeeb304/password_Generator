import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol=['!','@','#','$','%','^','&','*','(',')']
number=['1','2','3','4','5','6','7','8','9','0']
l=int(input("enter the number of letters:"))
s=int(input("enter the number of symbol:"))
n=int(input("enter the number from 0 to 9 :"))
password=[]
for i in range(1,l+1):
    char=random.choice(letters)
    password+=char
for i in range(1,l+1):
    char=random.choice(symbol)
    password+=char
for i in range(1,l+1):
    char=random.choice(number)
    password+=char
    
print(password)
random.shuffle(password)
pas=""
for char in password:
    pas+=char
print(pas)