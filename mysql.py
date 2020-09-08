import pymysql.cursors
import pandas


config = {
    'host':'140.116.247.183',
    'port':3306,
    'user':'iir',
    'password':'iir_5757',
    'db':'good_morning',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor,
}

connection = pymysql.connect(**config)

csv_file = ['作息_早安健康.csv', '高血壓_早安健康.csv', '睡眠_早安健康.csv', '運動_早安健康.csv', '糖尿病_早安健康.csv']

for csv in csv_file:
    _file = pandas.read_csv('./' + csv)
    _type = csv.split('_')[0]
    titles = _file['文章標題']
    abstracts = _file['摘要']
    urls = _file['文章url']
    img_urls = _file['縮圖url']
    for i in range(len(titles)):
        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO good_morning_table (title, abstract, url, img_url, type) VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(sql, (titles[i], abstracts[i], urls[i], img_urls[i], _type))
                connection.commit()
        except:
            pass