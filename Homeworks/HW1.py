#day2_homework1_question1

#I created a list and then i swaped the second half and first half by using reverse()

list=[1,2,3,4,5,6,7,8]
print(list)

list.reverse()
print(list)

#day2_homework1_question2

"""Firstly i create a value which is taken from the user and also i made 
this value int because input() is making string values. Then, i cretae a list by using
range(). n should be in the list thus i wrote 0 to n+1. Then i create a loop which 
is checking the value is even or not. """


n=int(input("Please enter a single digit integer: "))

list=(range(0,n+1))
for i in list:
  if i%2==0:
    print(i,"is even number")
    i=i+1
