#homework1

'''Firstly, i made a 2 lists. One of them has even numbers, one of them has odd 
numbers.Then, i merged these two lists. In addition, i sorted them.After that, i
multiplied all values in the list by 2. Finally, i printed the data type of all 
values in the list.'''

list1=[1,3,5,7,9]
list2=[2,4,6,8]
list1.extend(list2)
print(list1)
list1.sort()
print(list1)
list3=[x*2 for x in list1]
print(list3)
for a in list3:
    print(type(a))
