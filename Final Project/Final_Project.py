#FINAL PROJECT

"""First of all, i created the questions. Then i created a dictionary and assigned the answers to the questions. I created a score and set the score as 0. 
I used the for loop to calculate the score and checked if the answer was correct. The program adds 10 points to the score if the answer is correct. 
I used if statement in the step to check success. Finally,I wanted to print the answer key. I used pandas to print it. """

import pandas as pd

print("Welcome to the knowledge competition. Please pay attention to case sensitivity while writing answers, do not use numericals.")
q1="1-Which country's city is Seoul?"
q2="2-Which city is the capital of Turkey?"
q3="3-What color is banana?"
q4="4-Who is the first Turkish scientist to reciece the Nobel Prize?"
q5="5-What state of matter is water?"
q6="6-Who is Turkey’s first president?"
q7="7-Which region of Turkey does inclued Trabzon?"
q8="8-What is paper made of?"
q9="9-How many months is a year?"
q10="10-What is the full name of the instructor of the GAIH “Introduction to python” course?"

d={q1:"South Korea",q2:"Ankara",q3:"yellow",q4:"Aziz Sancar",q5:"liquid",q6:"Mustafa Kemal Atatürk",q7:"Black Sea",q8:"tree",q9:"twelve",q10:"Ömer Cengiz"}

score=0

for i in d:
  print(i)
  answer=input("Please, enter the answer: ")
  if answer==d[i]:
        score+=10

print("Your score:",score)

if score<=50:
  print("Unseccesfull")
else:
  print("Successfull!!")  

df1 = pd.DataFrame({'Questions':['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10'],
                    'Answers':['South Korea','Ankara','yellow','Aziz Sancar','liquid','Mustafa Kemal Atatürk','Black Sea','tree','twelve','Ömer Cengiz']
                   })

df1
