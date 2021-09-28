from flask import Flask, request, render_template,jsonify
import time
from flask_mysqldb import MySQL
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app=Flask(__name__)
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Mysql$#96'
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_DB']='flask_db'

mysql=MySQL(app)


@app.route('/db')
def index():
    cur=mysql.connection.cursor()
    #cur.execute("CREATE TABLE test(id INTEGER,name VARCHAR(20))")
    #cur.execute("INSERT INTO test VALUES(3,'abc')")
    #cur.execute("INSERT INTO test VALUES(4,'xyz')")
    #mysql.connection.commit()
    cur.execute("SELECT * FROM test")
    results = cur.fetchall()
    return render_template('db.html',results=results)


with open("counter.txt","r") as f:
     counter = int(f.readline())+1

@app.route("/count")
def main():
    with open("counter.txt","r") as r:
        counter = int(r.readline())+1
    with open("counter.txt","w") as w:
        w.write(str(counter))
    return render_template("counter.html",counter=counter)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/getTime", methods=['GET'])
def getTime():
    serverTime = time.strftime('%A %B, %d %Y %H:%M:%S')
    print(serverTime)
    return render_template('getTime.html',serverTime=serverTime)
@app.after_request
def before_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(debug=True )