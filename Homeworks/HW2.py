#day3

"""Firstly, i made an user access application as in the lecture and then 
i added user as dictionary, also i created name1 and password1 to access the name
and password in the dictionary.  """

user={"name":"Beyza","password":"123"}

name1=user["name"]
password1=user["password"]

name2=input("Enter your name: ")
password2=input("Enter your password: ")

if name2!=name1 and password2!=password1:
  print("Wrong name and password.")
elif name2!=name1 and password2==password1:
  print("Wrong name.")
elif name2==name1 and password2!=password1:
  print("Wrong password.")
else :
  print("Conguratilations! You logged in succesfully.")
