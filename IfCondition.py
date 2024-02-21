'''
1. Simple If

    if condition:
        statement
2. If/Else

    if condition:
        statement
    else:
        statement
3. Nested If/Else

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement

4. Ladder If/Else

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
        statement
'''
a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print(a," Is Max Number")
    else:
        print(c," Is Max Number")
elif b>c:
    print(b," Is Max Number")
else:
    print(c," Is Max Number")















