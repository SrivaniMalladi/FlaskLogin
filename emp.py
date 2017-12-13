import sqlite3

from flask import Flask,request,render_template


app = Flask(__name__)

Database = "empform.db"

def connect_db():
    return sqlite3.connect(Database)

@app.route('/list')
def list():
    db = connect_db()
    cur = db.execute("select empid,empname,desig,depart,sal from empform")
    entries = [dict(empid=row[0],empname=row[1],desig=row[2],depart=row[3],sal=row[4]) for row in cur.fetchall()]
    print(entries)
    db.close()
    return render_template('emp_list.html',html_entries = entries)

@app.route('/form')
def form():
    return render_template('empForm.html')

@app.route('/empform')
def empForm():
    eid = request.args.get('empid')
    ename = request.args.get('username')
    desig = request.args.get('designation')
    depart = request.args.get('department')
    sal = request.args.get('salary')

    db = connect_db()
    sql = 'Insert into empform(empid,empname,desig,depart,sal)values(?,?,?,?,?);'
    db.execute(sql,[eid,ename,desig,depart,sal])
    db.commit()
    db.close()
    return render_template('empDetails.html',h_eid=eid,h_ename=ename,h_desig=desig,h_depart=depart,h_sal=sal)

@app.route('/addEmpForm')
def addEmpForm():
    return render_template('empForm.html')

@app.route('/editProfile')
def editProfile():
    return "functionality has not yet coded !!!!"

@app.route('/deleteProfile')
def deleteProfile():
    return "Functionality has not yet added !!!!!"


if __name__ == '__main__':
    app.run(port=5000)


