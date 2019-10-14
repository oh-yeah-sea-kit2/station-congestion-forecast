# -*- coding: utf-8 -*-

import datetime
import os
import sqlite3

import logging
import scrapy
import psycopg2
import re

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class TenMinScrapyPipeline(object):
  def open_spider(self, spider: scrapy.Spider):
    # コネクションの開始
    url = spider.settings.get('POSTGRESQL_URL')
    self.conn = psycopg2.connect(url)

  def close_spider(self, spider: scrapy.Spider):
    # コネクションの終了
    self.conn.close()

  def process_item(self, item: scrapy.Item, spider: scrapy.Spider):
    sql = "INSERT INTO posts (url, title, time, date_start, date_end) VALUES (%s, %s, %s, %s, %s)"

    curs = self.conn.cursor()
    curs.execute(sql, (item['url'], item['title'], item['time'], item['date_start'], item['date_end']))
    # item['title'], item['url'], item['date']
    self.conn.commit()

    return item


# class TenMinScrapyPipeline(object):
#   _db = None

#   @classmethod
#   def get_database(cls):
#     cls._db = sqlite3.connect(
#       os.path.join(os.getcwd(), 'ten_min_scrapy.db'))
    
#     cursor = cls._db.cursor()
#     cursor.execute(
#       'CREATE TABLE IF NOT EXISTS post( \
#         id INTEGER PRIMARY KEY AUTOINCREMENT, \
#         url TEXT UNIQUE NOT NULL, \
#         title TEXT NOT NULL, \
#         date TEXT NOT NULL \
#       );')
#     return cls._db

#   def process_item(self, item, spider):
#     self.save_post(item)
#     return item
  
#   def save_post(self, item):
#     if self.find_post(item['url']):
#       return
#     db = self.get_database()
#     db.execute(
#       'INSERT INTO post (title, url, date) VALUES (?, ?, ?)', (
#         item['title'],
#         item['url'],
#         # datetime.datetime.strptime(item['date'], '%B %d, %Y')
#         item['date']
#       )
#     )
#     db.commit()
  
#   def find_post(self, url):
#     db = self.get_database()
#     cursor = db.execute(
#       'SELECT * FROM post WHERE url=?',
#       (url,)
#     )
#     return cursor.fetchone()
