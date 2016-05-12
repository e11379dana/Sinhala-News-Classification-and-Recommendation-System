<<<<<<< HEAD:NewsList/index.py
=======
import urllib2

import feedparser
import requests
from flask import *
>>>>>>> 5961b433700f44cd5f44919a42daf8d5cf44a514:SNCR_BackEnd/NewsList/index.py
from flask_restful import Resource

from mysql.connector import (connection)


class main(Resource):
    def get(self):
        db = connection.MySQLConnection(user='root', password='ilovepera',
                                         host='127.0.0.1',
                                         database='NewsData',
                                         charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

<<<<<<< HEAD:NewsList/index.py
=======
        # Drop table if it already exist using execute() method.
        cursor.execute("DROP TABLE IF EXISTS NewsOrder")

        # Create table as per requirement
        sql = """CREATE TABLE NewsOrder (
                 title  VARCHAR(1000), link  VARCHAR(1000), description VARCHAR(1000), pubDate VARCHAR(1000)) ENGINE = InnoDB DEFAULT CHARSET=utf8"""

        cursor.execute(sql)
        feed = feedparser.parse('http://www.hirunews.lk/rss/sinhala.xml')
        for entry in feed['items']:

            sql = "INSERT INTO NewsOrder(title,link,description) VALUES ('%s','%s','%s') " % (entry['title'],entry['link'],entry['description'])
            #print (entry['link'])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

>>>>>>> 5961b433700f44cd5f44919a42daf8d5cf44a514:SNCR_BackEnd/NewsList/index.py

        cursor.execute("SELECT * FROM NewsOrder")

        news = cursor.fetchall()
        newsList = []

        # print the rows
        for row in news:
            newsList.append({
                'title': row[0],
                'link': row[1],
                'description': row[2]
            })

        db.close()
        return (newsList)
