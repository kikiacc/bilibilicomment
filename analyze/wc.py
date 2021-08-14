import os

import jieba
import pymysql
from wordcloud import WordCloud
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
def statistic(list,stopword):
    word_dict={}
    for l in list:
        temp=jieba.cut(l[0])
        for t in temp:
            if t in stopword:
                continue
            if t in word_dict.keys():
                word_dict[t]+=1
            else:
                word_dict[t]=1
    return word_dict
def DrawWordCloud(words, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	wc = WordCloud(font_path='./fonts/simkai.ttf', background_color='black', max_words=2000, width=1920, height=1080, margin=5)
	wc.generate_from_frequencies(words)
	wc.to_file(os.path.join(savepath, 'commentscloudhuawei.jpg'))
# stopwords = open('./stopwords.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
# DrawWordCloud(statistic(get_comment("bytedance_bilibili"),stopwords))
stopwords = open('./stopwordshuawei.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
DrawWordCloud(statistic(get_comment("huawei_bilibili"),stopwords))

