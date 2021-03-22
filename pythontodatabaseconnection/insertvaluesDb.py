from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="insert into faculty(id,name,subject)values('100','ajay','datastructures')"

try:
    cursor.execute(sql)
    db.commit() #save changes
    print("query executed")
except Exception as e:
    print(e.args)
finally:
    db.close()