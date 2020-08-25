import sqlite3
import time
import datetime
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

bill = 0
 
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
                    print("You can go and have a checkup")
                    inpatient_outpatient = input("Are you an a An in-patient or b an out patient:  ")
                    if inpatient_outpatient == "a" or inpatient_outpatient == "in-patient" or inpatient_outpatient == "a An in-patient":
                        exit()
                    elif inpatient_outpatient == "b" or inpatient_outpatient == "out-patient" or inpatient_outpatient == "b an out-patient":
                        print("Yay")

                    

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
    login()        
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
            bill = bill + 200
            print(bill)
            db.commit()
    newUser()

             


