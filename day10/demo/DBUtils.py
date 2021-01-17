import pymysql
class DBUtils:
    host="localhost"
    user="root"
    password=""
    database="company"
    con=None
    cursor=None
    def __init__(self,host="localhost",user="root",password="",database="company"):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.con=pymysql.connect(host=self.host,
                                 user=self.user,
                                 password=password,
                                 database=database)
        self.cursor=self.con.cursor()

#增删改 ：
    def update(self,sql,param,mode="1"):#1：执行一条   2：多条
        if mode=="1":
            self.cursor.execute(sql,param)
        else:
            self.cursor.executemany(sql,param)


    def select(self,sql,param,mode="all",size=1):
        self.cursor.execute(sql,param)#执行sql语句
        if mode=="all":#判断取值模式
            return self.cursor.fetchall()
        elif mode=="many":
            return  self.cursor.fetchmany(size)
        elif mode=="one":
            return self.cursor.fetchone()
    def releaseConnection(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()

'''db = DBUtils()
sql="select * from t_employees where ename=%s"
param=[["关二爷"]]
result=db.select(sql,param,mode="all")
print(result)
db.releaseConnection()'''

