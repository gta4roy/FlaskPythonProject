import flask 
import sqlite3
from flask import request ,jsonify

app= flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def home():
    return "<H1>Hello Work Welcome to Flask Based Api </H1>"

@app.route('/health',methods=['GET'])
def server():
    return "<H1>Server is at Good Health </H1>"


@app.route('/api/v1/resources/books/all',methods=['GET'])
def api_all():
    try:
      dbConnection = sqlite3.connect('books.db')
      cur = dbConnection.cursor()
      cur.execute('select * from book')
      return  jsonify(cur.fetchall())
    except Exception as e:
      print(e)
      pass


@app.route('/api/v1/resources/books',methods=['GET'])
def api_id():
    try:
      if 'id' in request.args:
        id = int(request.args['id'])
      else:
        return "Error : No if field provided . Please specify a proper "

      dbConnection = sqlite3.connect('books.db')
      cur = dbConnection.cursor()
      cur.execute('select * from book where id='+str(id))
      result = cur.fetchone()
      return jsonify(result)
    except Exception as e:
      print(e)
      pass


@app.route('/api/v1/resources/books/save',methods=['GET','POST'])
def save():
    try:
      print("Request Received")
      content = request.get_json(force=True)
      #print(content.keys())
      print("Content Recieved ",content)

      title = content['title']
      author = content['author']
      id_number = content['id']
      year = content['Year']

      dbConnection = sqlite3.connect('books.db')
      cur = dbConnection.cursor()
      sqlQuery =('insert into book (id,title,author,year) values ('+str(id_number)+','+title+','+author+','+str(year)+')')
      print(sqlQuery)
      count =cur.execute(sqlQuery)
      dbConnection.commit()
      print("Count after commit ",count)
      print("Successfully commited one record into book table...",cur.rowcount)
      cur.close()
    except Exception as e:
      print(e)
    finally:
        print("SQL Connection have been closed ")
        return


app.run()
