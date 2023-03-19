

def Q_master():
    while True :
        print("\t\t\t\tWelcome Master \n \t Shake your Brain and add some Challenging Question\n")
        print("\n PRESS 1 FOR ADD QUESTION.\n PRESS 2 FOR VIEW QUESTION.\n PRESS 3 FOR DELETE QUESTION.\n PRESS 4 FOR EXIT\n\n")
        m_choice = int(input("Which Operation You want to Perform : "))


        if m_choice == 1 :
            str_Q = input("Enter Your Question : ")
            str_O1 = input("Enter Option 1 : ")
            str_O2 = input("Enter Option 2 : ")
            str_A = input("Enter Answer : ")

            file = open("Question.txt","w")
            file.write(str_Q+"\n")
            file.write(str_O1+"\n")
            file.write(str_O2+"\n")
            file.write(str_A+"\n")
            file.close()

        elif m_choice == 2 :
            file = open("Question.txt","r")
            print(file.read())
            file.close()
        
        elif m_choice == 3 :
            file = open("Question.txt","r")
            file.close()
        
        elif m_choice == 4 :
            break

    
def Q_cracker() :
    print("na")
    



print("\n\t\tWelcome to Tops Quiz Gaming Challenge\n")

print("\t\tPLEASE SELECT YOUR ROLE : \n\n")

print("\t\t\t--> Quiz Master \t (Press 1)")
print("\t\t\t--> Quiz Cracker \t (Press 2)")

user = int(input("Enter your role : "))
if user == 1 :
    Q_master()

else :
    Q_cracker


    
