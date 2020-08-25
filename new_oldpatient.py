import sqlite3
conn = sqlite3.connect('new_user.db') 
cursour = conn.cursor()
    
cursour.execute("CREATE TABLE IF NOT EXISTS new_user(fName TEXT, sName TEXT)")

cursour.execute("INSERT INTO new_user VALUES('Munene', 'Muondu')")
                
cursour.execute("INSERT INTO new_user VALUES('Malli', 'Mithage')")
conn.commit()
                

