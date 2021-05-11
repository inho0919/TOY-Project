import psycopg2
import json

hostname = "[호스트이름]"
username = "[유저이름]"
password = "[비밀번호]"
port = "[포트번호]"
db_name = "[데이터베이스 이름]"
    
def create(ids, title, texts):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "INSERT INTO board(id, title, content) VALUES('"+ids+"', '"+title+"','"+texts+"');"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Create)"

def read():
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "SELECT * FROM board;"
        cur.execute(sql)
        a = cur.fetchall()
        a = json.dumps(a)
        a = json.loads(a)
        conn.commit()
        conn.close()
        return a
    except:
        return "Error (Read)"

def update(num, ids, title, texts):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "UPDATE board SET no='"+num+"', id='"+ids+"', title='"+title+"', content='"+texts+"' WHERE no='"+num+"';"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Update)"

def delete(no):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "DELETE FROM board WHERE no = '"+no+"';"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Success"
    except:
        return "Error (Delete)"

def datas(num):
    try:
        conn = psycopg2.connect("host='"+hostname+"' user='"+username+"' password='"+password+"' port='"+port+"' dbname='"+db_name+"'")
        cur = conn.cursor()
        sql = "SELECT * FROM board WHERE no = '"+num+"';"
        cur.execute(sql)
        a = cur.fetchall()
        a = json.dumps(a)
        a = json.loads(a)
        conn.commit()
        conn.close()
        return a
    except:
        return "Error (Read)"

