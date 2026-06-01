#hello world
print("hello world")
print("my name is swornim maharjan")

#sum and difference
print(30 + 2)
print(44 - 33)
print(3.14 * 3 * 3)
print("this is the area of the circle is:", 3.14 * 3 * 3)

#value
name = ("swornim maharjan")
age = 18
print(name, age)
name = ("swornim maharjan")
age = 18
print("my name is",name)
print("i am",age,"years old")

#pointer
name=("swornim maharjan")
xyz=name
print(xyz)

#type
name = ("swornim maharjan")
age = 18
print(type(name))
print(type(age))

#input variables
a=1
b=23
sum=a+b
print(sum)

#arithmetic operator
a=4
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #a^b
#OR
a=4
b=6
print((a+b),(a-b),(a*b),(a/b),(a%b),(a**b))

#relational operators(result in boolean form i.e true or false)
a=40
b=30
print(a==b) #false
print(a!=b) #true
print(a>=b) #true
print(a>b) #true
print(a<=b) #false
print(a>b) #false

#assignment operators
a=10
b=a+10 #we can also use a+=10 and vise versa for other(+-*/)
print(b)

#logical operators
#not gate
a=10
b=20
print(not (a>b)) #false but not gate changes it into true
#and gate
a=True
b=False
print("And gate:",a and b)
#or gate
print("Or gate:",a or b)
#extraaaaaaaa
a=20
b=33
print("the expression is:",a>b or a<b)

#type conversion
#(integer to float and vise versa)
#float into integer
a=5.3
b=int("4")
print(type(b))
print(a+b)
#or integer into float
a=5.3
b=float("4")
print(type(b))
print(a+b)
# float/integer into string
a=3.14
a=str(a)
print(type(a))

#input statement
#input("your name")

#also can be written as:
name=input("your name")
print("my name is:",name)


