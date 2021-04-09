#day4_homework3
#course grade apllication

"""Firstly, i created 5 students from the user then i made a function that 
calculates students grades. After that i created dictionary which is holding 
student name and grade information. I created a list and transferred the values 
from the dictionary. Then, i sorted them but sort() is sorting lower to highest 
so that's why i used also reverse(). """


student1=input("Enter student1 name: ")
student2=input("Enter student2 name: ")
student3=input("Enter student3 name: ")
student4=input("Enter student4 name: ")
student5=input("Enter student5 name: ")

def passinggrade(x,y,z):
  grades={"midterm grade:":x,"final grade:":y,"project grade:":z}
  passingGrade= x*0.3 + y*0.3 + z*0.4
  return passingGrade

studentsinformations={student1:passinggrade(50,60,80),student2:passinggrade(60,70,80),student3:passinggrade(70,80,90),student4:passinggrade(50,90,85),student5:passinggrade(30,90,65),}

print(studentsinformations)

list1=list(studentsinformations.values()) 

list1.sort()
list1.reverse()

print(list1)
