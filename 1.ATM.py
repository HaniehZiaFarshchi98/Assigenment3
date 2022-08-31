user_password= 1234
counter=0

for i in range(3):
    password=int(input("please enter password: ")) 

    if password == 4321:
        print("we called to police!")  
        break  
    elif password != user_password:
        print("password is incorrect")
        counter +=1
    else:
        print ("welcom!")
        break
if counter >= 3:
    print("your account is locked")
    
       