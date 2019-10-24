#Kephryn Merkley
#Geometry Homework
#9-11-19
#Error checking
#Line 30, the larger the answer, it ruins the square
#Missing Input() at the end to keep the code running (Logic error)
#Last square is actually a cube
#No label to final displayed number
#No label to lengths on squares
#Can be simplified a little bit.
#Doesn't support floats (Logical Error)
#Taya, Jessica, Isaac, Kaydon

def menu():
    while True:
        intro("example","x","y","z","a","b")
        choice = input("pick an option 1,2,3, or 4")
        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            verify = quit_verify()
            if verify:
                break

        else:
            print("that's not an option")
menu()
input("press enter to exit")

answer = str(input("Are you a student?"))
if answer == 'yes': print("Let's get this homework done!")
else: print('then get out of here!')

print("""Okay let's figure out the perimeter of your square""")
length = input("what is the length of your square?")
width = input("what is the width of your square?")
length = int(length)
width = int(width)
answer2 = (length + length + width + width)
#this is the perimeter of the square
Sqr_perim = str.format("""
          {0}      
      _________  
     |         | 
     |         | 
{1}    |         |{1}
     |         | 
     |_________| 
             
          {0}
          """,length,width)
print(Sqr_perim)
print(answer2)
print("""Okay let's figure out the area of your square""")
length = input("what is the length of your square?")
width = input("what is the width of your square?")
length = int(length)
width = int(width)
answer3 = (length * width)
sqr_area = str.format("""
          
          ___
        _/ | \\_
      _/   |   \\_ 
    _/     |     \\_
   |_      |      _|
   | \\_    |    _/ |
   |   \\_  |  _/   |
   |     \\_|_/     | 
   |       |       |
   |       |       |
   |_      |      _|
     \\_    |    _/
       \\_  |  _/ 
         \\_|_/          

""")
print(sqr_area)
print(answer3)

print("""okay let's figure out the circumference of your circle""")
