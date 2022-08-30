print("units: 1.h-->s   2.s-->h ")

time=int(input("please enter time:"))
unit=input("please select unit:")

if unit == '1':
    h_to_s = (time * 3600)
    print (h_to_s , "s")
elif unit == '2':
    s_to_h =(time // 3600)
    print (s_to_h , "h")
else :
    print ("please select again!") 