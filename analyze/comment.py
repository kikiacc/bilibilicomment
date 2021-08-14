import pymysql
from snownlp import SnowNLP
import numpy as np
from matplotlib import pyplot as plt
def get_comment(table_name):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='data_analyze',
        charset='utf8mb4'
    )
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
    return list
def get_gradelist(list):
    grade=[]
    for l in list:
        try:
            ll=SnowNLP(l[0])
            grade.append(ll.sentiments)
        except:
            continue
    print(len(grade))
    return grade
def draw(list):
    plt.hist(list, bins=np.arange(0, 1, 0.02))
    plt.show()
huawei_grade=get_gradelist(get_comment("huawei_bilibili"))
bytedance_grade=get_gradelist(get_comment("bytedance_bilibili"))
draw(huawei_grade)
draw(bytedance_grade)

