from flask import redirect
from werkzeug.security import check_password_hash

from config.database import db
cursor = db.cursor()

def User(email,passwordCod):
    print(passwordCod)
    try:
        cursor.execute("SELECT * FROM users WHERE email = '"+email+"'")
        myresult = cursor.fetchone()
        if myresult != None:
            print("usuario registrado")
        else:
            print("registrado exitosamente")
        print("Query Excecuted successfully")
    except:
        db.rollback()
        print("Error")