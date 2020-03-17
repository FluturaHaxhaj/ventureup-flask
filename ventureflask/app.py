from flask import Flask, request
import psycopg2
import json
import datetime
# from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

conn_string = "host='localhost' dbname='employeecheckinsystem' user='emp' password='emp'"
conn = psycopg2.connect(conn_string)
cursor=conn.cursor()

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://emp:emp@localhost:5432/employeecheckinsystem"
# db = SQLAlchemy(app)
# app = Flask(__name__)



@app.route('/employee', methods=['POST','GET'])
def hello_world():
    content = ''
 
    if request.method == "POST":
        content = request.get_json()
        query = '''insert into Puntori (emri,mbiemri,nrTel ) values(\'{}\' , \'{}\', \'{}\' );'''.format(content.get("emri"),content.get("mbiemri"),content.get("nrTel"))
        cursor.execute(query)
        conn.commit()
        return json.dumps({'message':'Punetori u regjistrua me sukses'})
    elif request.method=="GET": 
        query = '''SELECT * FROM Puntori'''
        cursor.execute(query)
        result=cursor.fetchall()
        print(result)
        return(result)
    return 'nothing happened'
        # cursor.close()
        # conn.close()

@app.route('/attendence', methods=['POST','GET'])
def attendence():
    if request.method == "POST":
        content = request.get_json()
        cursor.execute("INSERT INTO evidenca (p_id,check_in) VALUES (%s, %s)", (content.get("p_id"), datetime.datetime.now()))
        conn.commit()

    # elif request.method == "GET":
        return 'Attendence added'
    else:
        return 'Somethin happened'

    

