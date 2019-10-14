# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TenMinScrapyItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  pass

class Post(scrapy.Item):
  url = scrapy.Field()
  time = scrapy.Field()
  title = scrapy.Field()
  date = scrapy.Field()
