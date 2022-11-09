from flask import Flask, render_template, request, session, redirect, url_for
import sqlalchemy

app = Flask(__name__)
app.secret_key = "hello"

'''class Student(db.Model):
    _tablename_= "Student"
    RollNo  = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Name = db.Column(db.String,nullable=False)
    Email = db.Column(db.String, nullable=False, unique=True)
    Password = db.Column(db.String, nullable=False)

class Teacher(db.Model):
    _tablename_="Teachers"
    T_code = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Tname = db.Column(db.String, nullable=False)
    Temail = db.Column(db.String, nullable=False, unique=True)
    Tpassword = db.Column(db.String, nullable=False)

class Admin(db.Model):
    _tablename_="Admins"
    Aid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Aname = db.Column(db.String, nullable=False)
    Aemail = db.Column(db.String, nullable=False, unique=True)
    Apassword = db.Column(db.String, nullable=False)'''

@app.route("/", methods = ["GET", "POST"])
def first():
    return render_template("index.html")

@app.route("/slogin", methods = ["GET", "POST"])
def slogin():
    sname = request.form("username")
    spass = request.form("password")
    session["user"]=suser
    return render_template("Student_login.html")

@app.route("/ssess", methods = ["GET", "POST"])
def suser():
    if  "user" in session:
        user = session["user"]
        return render_template("sdash.html", userd = user)
    else:
        return redirect(url_for("slogin"))

@app.route("/tlogin", methods = ["GET", "POST"])
def tlogin():
    tname = request.form("username")
    tpass = request.form("password")
    return render_template("teacher_login.html")

@app.route("/alogin", methods = ["GET", "POST"])
def alogin():
    aname = request.form("username")
    apass = request.form("password")
    return render_template("admin_login.html")

@app.route("/logout", methods = ["GET", "POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("first"))



if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        debug=True,
        port = 5050
    )