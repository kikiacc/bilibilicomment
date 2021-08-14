import pymysql
from snownlp import SnowNLP
import numpy as np
from matplotlib import pyplot as plt
conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='data_analyze',
        charset='utf8mb4'
    )
table_name="huawei_bilibili"
cursor = conn.cursor()
sql = "select comment from "+table_name+";"
cursor.execute(sql)
res = cursor.fetchall()
print(type(res))
list = []
for r in res:
    try:
        list.append(r)
    except:
        continue
print(len(list))
conn.commit()
cursor.close()
conn.close()
grade=[]
for l in list:
    print(type(l))
    try:
        ll=SnowNLP(l)
        if(0<=(ll.sentiments)<=1):
            grade.append(ll.sentiments)
    except:
        continue
print(len(grade))