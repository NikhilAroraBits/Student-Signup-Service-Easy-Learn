from flask import Flask, render_template, redirect, url_for, session,request
from flask_mysqldb import MySQL
import MySQLdb
import random

app = Flask(__name__)
app.secret_key = "123456"

app.config["MYSQL_HOST"] = "scalableservicesassignment.cz1kzfagdqhy.ap-south-1.rds.amazonaws.com"
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "123Amazon"
app.config["MYSQL_DB"] = "UserInfo"

db = MySQL(app)

@app.route('/StudentSignup', methods=['GET', 'POST'])
def StudentSignup():
    if request.method == 'POST':
        if 'email' in request.form and 'password' in request.form and 'name' in request.form:
            email = request.form['email']
            password = request.form['password']
            name = request.form['name']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            choices = list(range(100))
            random.shuffle(choices)
            id= 100000 + choices.pop()
            cursor.execute("INSERT INTO UserInfo.logininfo (id, name, email, password) VALUES (%s, %s, %s, %s)", (id, name, email, password))
            db.connection.commit()
            return 'Signup Successful !!'
           

    return render_template("SignUp.html")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
