age = input("Enter your age : ") 
age = int(age)
if(age>18):
    print("You can drive all domestic vehicles")

elif(age==18):
    print("You are an awsome teen!!!")
else:
    if(age==16):
        print("You can only drive non geared vehicles")
    elif(age==17):
        print("You can only drive non geared vehicles")
    else:
        print("You need to wait for", 16-age, "years to drive a non geared vehicle and you need to wait for", 18-age, "years to drive all domestic vehicles")