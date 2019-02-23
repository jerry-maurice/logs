# !/usr/bin/env python3
# This program create a report from a databases called news
# Created by Jerry Maurice
import psycopg2
from datetime import datetime

# name of database
DBNAME = "news"


def topThreeLog():
    # connect to database
    db = psycopg2.connect(database=DBNAME)
    query = db.cursor()
    query.execute("select title, count(path) from articles join log "
                  + "on split_part(path::TEXT,'/',3) = slug group by title "
                  + "order by count(path) DESC limit 3")
    posts = query.fetchall()
    db.close()
    return posts


def mostPopularAuthor():
    # connect to database
    db = psycopg2.connect(database=DBNAME)
    query = db.cursor()
    query.execute("select authors.name, count(path) from articles join "
                  + "log on split_part(path::TEXT,'/',3) = slug inner join "
                  + "authors on authors.id = articles.author group by name "
                  + "order by count(path) DESC")
    posts = query.fetchall()
    db.close()
    return posts


def errorRequest():
    # connect to database
    db = psycopg2.connect(database=DBNAME)
    query = db.cursor()
    query.execute("select date(time),round(((count(*) filter (where "
                  + "status not like '200 OK')*100)::decimal)/"
                  + "count(status)::decimal,2) as v from log group by "
                  + "date(time) order by v DESC limit 1")
    posts = query.fetchall()
    db.close()
    return posts


if __name__ == '__main__':
    # getting the top three most viewed articles
    print("Top three most viewed articles: ")
    for a, b in topThreeLog():
        print(a+" - "+str(b)+" views")
    # who are the most popular author of all time
    print("Most popular articles authors of all time: ")
    for a, b in mostPopularAuthor():
        print(a+" - "+str(b)+" views")
    # higher than 1% request leading to error
    print("When more than 1% lead to errors: ")
    for a, b in errorRequest():
        print(datetime.strftime(a, '%b %d, %Y')+" - "+str(b)+"% errors")
