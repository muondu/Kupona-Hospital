import sqlite3
import time
import datetime
from diseases import *
from doctors_malaria import *
from doctors_corona import *
from pharamsy import *
conn = sqlite3.connect('new_user.db') 
c = conn.cursor()

now = datetime.datetime.now()
hour = now.hour
if hour < 12:
    print("Good morning")
elif hour > 12 and hour < 18:
    print("Good afternoon")
elif hour > 18 and hour < 19:
    print("Good evening")
else:
    print('Good night.')

 
print("Hi. Welcome to Kupona hospital where our patients all ways get cured and been given the write medicine with professional doctors who have been working for 20 years")
new_person_or_not = input("Are you new. Yes(y) or No(n)? ")
if new_person_or_not == "n" or new_person_or_not == "no" or new_person_or_not == "N" or new_person_or_not == "No":
    def login():
        for i in range(3):
            fName = input("PLS enter your first name: ")
            sName = input("PLS enter your second name: ")
            with sqlite3.connect('new_user.db') as db:
                cursour = db.cursor()
            find_user = ('SELECT * FROM new_user WHERE fName = ? AND sName = ?')
            cursour.execute(find_user,[(fName), (sName)])
            results = cursour.fetchall()
            if results:
                for i in results:
                    buda = str(i)
                    print("Welcome " +buda)
                    print("You have been charged 50 sh")
                    global old_person_bill
                    old_person_bill = 50
                    print("You can go and have a checkup")
                    def inpatient_outpatient_funct():
                        inpatient_outpatient = input("Are you an a An in-patient or b an out patient:  ")
                        if inpatient_outpatient == "a" or inpatient_outpatient == "in-patient" or inpatient_outpatient == "a An in-patient":
                            print("We dont have that service now")
                            exit()
                            
                        elif inpatient_outpatient == "b" or inpatient_outpatient == "out-patient" or inpatient_outpatient == "b an out-patient" or inpatient_outpatient == "out patient":
                            def out_patient():
                                print(diseases)
                                which_disease = input("""
                                    Hi. These are the diseases above with their price. 
                                    Which disease are you suffering from?
                                    """)
                                if which_disease == "malaria" or which_disease == "Malaria":
                                    print("These are the doctors available")
                                    print(doctors)
                                    def doctors_func():
                                        which_doctor = input("Which doctor do you want: ")
                                       
                                        if which_doctor == "Dr.Jane" or which_doctor == "Dr.Mathew":
                                            print("You have been charged 200 sh")
                                            global doctor_disease_bill
                                            doctor_disease_bill = 200
                                            print("You can go to the doctor")

                                            print("Welcome to the pharmasy.")   
                                            print("These are the medicine of Malaria.")
                                            print(pharmasy_malaria)
                                            which_medicine = input("Which of the medicine above do you want:")
                                            if which_medicine == "Malarone" or which_medicine == "Quinine" or which_medicine == "Mefloquine" or which_medicine == "Primaquine phospate":
                                                print("The price of that medicine 700 sh")
                                                global medicine_bill
                                                medicine_bill = 700
                                                total_bill = old_person_bill + doctor_disease_bill  + medicine_bill + 200
                                                print("Your total bill is " +  str(total_bill))
                                                payment = int(input("Enter the amount: "))
                                                if payment > total_bill:
                                                    change = payment - total_bill
                                                    print("Your change is " + str(change))
                                                elif payment == total_bill:
                                                    print("Thankyou and have a lovely day")
                                                elif payment < total_bill:
                                                    print("You have paid less money. Please pay the remaining amount.")
                                                    payment - total_bill
                                                    exit()
                                                else:
                                                    print("I did not understand you")
                                            
                                        else:
                                            print("I did not understand you")
                                            doctors_func()
                                    doctors_func()
                                elif  which_disease == "Corona" or which_disease == "corona":
                                    print(doctors_corona)
                                    def doctors_func():
                                        which_doctor = input("Which doctor do you want: ")
                                        if which_doctor == "Dr.Kamau" or which_doctor == "Dr.Mary":
                                            print("You have been charged 200 sh")
                                            global doctor_disease_bill
                                            doctor_disease_bill = 200
                                            print("You can go to the doctor") 
                                            print("Welcome to the pharmasy.")   
                                            print("These are no medicines for Corona. Sorry")
                                            total_bill = old_person_bill + doctor_disease_bill  +  200
                                            print("Your total bill is " +  str(total_bill))
                                            payment = int(input("Enter the amount: "))
                                            if payment > total_bill:
                                                change = payment - total_bill
                                                print("Your change is " + str(change))
                                            elif payment == total_bill:
                                                print("Thankyou and have a lovely day")
                                            elif payment < total_bill:
                                                print("You have paid less money. Please pay the remaining amount.")
                                                payment - total_bill
                                                exit()
                                            else:
                                                print("I did not understand you")
                                        
                                        
                                        else:
                                            print("I did not understand you")
                                            doctors_func()
                                    doctors_func()
                                else:
                                    print("I did not understand you")
                                    out_patient()
                                    
                            out_patient()                       
                            
                        else:
                            print("Please input the write thing") 
                            exit()  
                    inpatient_outpatient_funct()        
                    

            else:
                print("First name and last name are not found")
                again = input("Do u want to try again?(y/n): ")
                if again == "n" or again == "N" or again == "no" or again == "No":
                    print("Good Bye")
                    time.sleep(1)
#                return('exit')
                elif again == "y" or again == "Y" or again == "yes" or again == "Yes":
                    login() 
                else:
                    print("I did not understand you.")
            
                break       
    login() 
    
    exit()
elif new_person_or_not == "y" or new_person_or_not == "yes" or new_person_or_not == "Y" or new_person_or_not == "Yes":
    def newUser():
            fName = input("Please enter your first name:  ")
            with sqlite3.connect('new_user.db') as db:
                cursour = db.cursor()
            findUser = ('SELECT * FROM new_user WHERE fName = ?')
            cursour.execute(findUser,[(fName)])
            sName = input("Enter your second name : ")
            insertData = '''INSERT INTO new_user('fName', 'sName') VALUES(?,?)'''
            cursour.execute(insertData,[(fName),(sName)])
            print("Loading...")
            time.sleep(3)
            print("Succesfully done")
            print("The price of the new card is 200.")
            # bill += 200
            # print(bill)
            db.commit()
    newUser()
else:
    print("I did not understand you")

             


