x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
a = input("Choose operator '+', '-', '*', '/' : ")
if(a=="+"):
    print(x+y)
elif(a=="-"):
     print(x-y)
else:
     if(a=="/"):
         print(x/y)
     elif(a=="*"):
          print(x*y)
     else:
          print("\nPlease choose a operator \n Program Terminated!!!")

