from flask import redirect
from werkzeug.security import check_password_hash
from config.database import db
cursor = db.cursor()

from flask import redirect
from config.database import db
cursor = db.cursor()

def signUser(email,password):
    sql = "SELECT * FROM users WHERE email = %(email)s and password = %(password)s"
    cursor.execute(sql,{'email':email,'password':password})
        
    results= cursor.fetchone()
    return results