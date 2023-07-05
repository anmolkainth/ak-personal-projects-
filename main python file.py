'''special operators
** exponent
// floor division(eg gives 6.04 as 6)
% modulo operator(tells remainder)
|  union(only in sets) 
& intersection (only in sets)

'''


# import math
# age= int(input("age : "))
# print(math.gcd(3,6))
# '''if (age<18)
#     print("yo passed")'''


# a = 45
# b = "Anmol"
# c = 58.87
# # anmol kainth = 5
# # print(a+4)

# Type_A = type(a)
# Type_B = type(b)
# # print(Type_A)
# # print(Type_B)
# #a = "45.05"
# a = "45"
# Type_A = type(a)
# # print(Type_A)
# a = int(a)
# #a = str(a)
# print(a+c)

# name = '''Anmol
# Kainth'''
#print (name[:4])
# name='  anmol  '
# print(name.strip())
# print(name)
# name=("Anmol")
# print(len(name))
# var =  name.lower()
# print(var)
# var = name.replace("m", "b") #be careful of lower case and upper case 
# print(var)
# name = "Anmol, Daviner, Anita"
# var = name.replace(", ", '\n')
# print(var)

# stri = "This is a "
# name1 = "Anmol"
# name2 = "Davinder"
# stri2 = "This is not a"
# print(stri + stri2)
# print(stri + name1)
# temp1 =  "this is {} and he is his brother {}.".format(name1, name2)#by default {0},{1}
# temp2 =  "this is {1} and he is his brother {0}.".format(name1, name2)
# print(temp1)
# print(temp2)
# temp =f"this is {name1} and he is his brother {name2}."#'f'string makescommand of temp1 and temp2 easy to use
# print(temp)

'''
Python collections:
1. List
2. Tuple
3. Set
4. Dictionary
'''

                                                      #List
# lst = [67,8,3,2,53]
# var= type(lst)
# var= lst[0:3]
# lst[2]= 25 #replaces the item at position 2(i.e 3) with 25
# lst.append(100)#addd the item at last of the list
# lst.insert(1,80)#inserts/replaces item at that place(i.e it puts 80 at 1 position(8))
# lst.remove(67)
# lst.pop()#removes last element from list
# del lst[3]
# lst.clear()
# var= lst
# print(var)


                                                            #  tuple(you can't change value/item in tuple)
# a= ("Anmol", "Davinder", "Anita")
# var= a
# a= list(a)#type casting chages type (eg changes int to str , tuple to list)
# var = type(a)
# print(var)

                                #  set(just like chapter sets in maths (numbers don't repeat, can do union intersection etc)  )
    
# s1 = {24,3,4,3,4,4,56,7,7,5,4}
# s2 = {18,20,3}
# s1.add(3456)
# s1.update([12,45,6,7,6,78])
# s1.discard(1)#better then remove because don't show error even when that item is not in set(don't understand try it)
# print (s1)
# print(s1 | s2)# '|' is operator for union
# print(s1 & s2)# '&' is operator for intersection


                                                   #dictionary
# anmolDict = {
#     "Name": "Anmol",
#     "Class": "11th",
#     "Marks": 70,
#     "Hours in school": 6
# }                                                 
# print(anmolDict)
# anmolDict["Name"] = "Anmol Kainth"
# print(anmolDict["Name"])
# print(anmolDict)

                                            #  conditional
# age = input("Enter your age : ") 
# age = int(age)
# print(type (age))                                           
# if(age>18):
#     print("You can drive")
# elif(age==18):
#     print("You are an awsome teen")    
# else:
#     print("You can not drive")    

                                                #loop

# for i in range(0,1000):
#     print(i) 
# li = [1,56,"lol"]
# li={2,34,5,6,677,6}#sets
# for item in li:
#     print(item)

# i = 0
# while(i<100):
#     print(i+1)
#     if i == 78:
#       break
#     i= i+1

# i = 0
# while(i<100):
#     i= i+1
#     if i == 78:
#      continue
#     print(i+1)

                                                    # Functions
# def greet():
#     print("Good morning sir")
#     print("YO!")

# greet()
# greet()

# def sum(a, b):
#     c = a + b                                           
#     return c
# d = sum(35 , 67)
# print(d)


                                                 #Template
# class Employee:
#     def __init__(self, gname, gsalary):
#      self.name = gname
#      self.salary = gsalary

# anmol = Employee("Anmol" , 34)
# print(anmol.name)
# print(anmol.salary)
