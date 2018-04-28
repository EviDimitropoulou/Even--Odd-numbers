#Ευη Δημητροπούλου
import random as rn

while True:
    x=rn.randint(0,36)
    

    if x==0:
       print("Zero",x)
   
    elif 1<=x<=17:
        print("Small Number",x)

    elif 18<=x<=36:
         print("Big Number",x)
      
    if 1<=x<=10 or 19<=x<=28:
         if x%2==0:
             
             print("even")
             print("blacj")
             data = input("q for exit or enter for next random number: ")
             print("\n")
             if data=='':
              continue
             elif data=='q':
              break
         elif x%2==1:
            
             print("odd")
             print("red")
             data = input("q for exit or enter for next random number: ")
             print("\n")
             if data=='':
              continue
             elif data=='q':
              break
         break
    if 11<=x<=18 or 29<=x<=38:
         if x%2==0:
             
             print("even")
             print("red")
             data = input("q for exit or enter for next random number: ")
             print("\n")
             if data==' ':
              continue
             elif data=='q':
              break
         elif x%2==1:
             print("\n")
             print("odd")
             print("black")
             if data=='':
              continue
             elif data=='q':
              break
         break


