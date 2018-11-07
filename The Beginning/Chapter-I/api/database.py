import sqlite3 as lite
import sys

def get_tables():
    con = lite.connect('TestEmails.db')  
    tables = con.execute("SELECT name FROM sqlite_master WHERE type='table';")
    names = []
    for name in tables:
        names.append(name[0])
    con.close()
    return names

def check_if_table_exists(name):
    if name in get_tables():
        return True
    else:
        return False

def insert(email):
    con = lite.connect('TestEmails.db') 
    if(check_if_table_exists("Emails")):
        con.execute("INSERT INTO Emails VALUES(?);" , [(email)])            
        con.commit()
        con.close()
        print("[#] The value '%s' has been successful added in Emails table!" % email) 
    else:
        print("[ ] Creating table 'Emails' ...")
        con.execute("CREATE TABLE Emails(email TEXT)")
        print("[*] The table 'Emails' has benn created!")
        con.execute("INSERT INTO Emails VALUES(?);" , [(email)])            
        con.commit()
        con.close()
        print("[#] The value '%s' has been successful added to table!" % email)

# only for testting

def show_table():
    con = lite.connect('TestEmails.db')  
    rows = con.execute("SELECT * FROM Emails;")
    for row in rows:
        print(row)
    con.close()




