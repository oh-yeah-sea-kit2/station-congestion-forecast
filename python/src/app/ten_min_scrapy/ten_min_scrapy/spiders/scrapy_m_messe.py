# -*- coding: utf-8 -*-
import scrapy
from ..items import Post
import urllib.parse
import re
import datetime

class ScrapyMMesseSpider(scrapy.Spider):
  name = 'scrapy_m-messe'
  allowed_domains = ['www.m-messe.co.jp']
  start_urls = ['https://www.m-messe.co.jp/event/']

  def parse(self, response):
    # url_list = []
    for post in response.css('div.eventTopics > div'):
      # 欲しいデータ
      # 日付、時間（期間）
      # イベント名、内容
      url=post.css('div.readmore > a::attr(href)').extract_first().strip()
      url_child = urllib.parse.urljoin(self.start_urls[0],url)
      yield scrapy.Request(url_child, callback=self.parse_child, meta={'url': url_child})
  
  def parse_child(self, response):
    title = response.css('div.articleMain > dl > dd:nth-child(2)::text').extract_first().strip()
    date = response.css('div.articleMain > dl > dd:nth-child(6)::text').extract_first().strip()
    time = response.css('div.articleMain > dl > dd:nth-child(8)::text').extract_first().strip()
    # detail = response.css('div.articleMain > dl > dd:nth-child(4)::text').extract_first().strip()
    # 
    jst = datetime.timezone(datetime.timedelta(hours=9))
    repatter1 = re.compile(r'^(\d{4})年(\d{2})月(\d{2})日\(.\)～(\d{4})年(\d{2})月(\d{2})日\(.\)$')
    repatter2 = re.compile(r'^(\d{4})年(\d{2})月(\d{2})日\(.\)$')
    result1 = repatter1.match(date)
    result2 = repatter2.match(date)
    if result1:
      date_start = datetime.datetime(
        year=int(result1.group(1)),month=int(result1.group(2)),day=int(result1.group(3)),
        hour=0,minute=0,second=0,tzinfo=jst
      )
      date_end = datetime.datetime(
        year=int(result1.group(4)),month=int(result1.group(5)),day=int(result1.group(6)),
        hour=0,minute=0,second=0,tzinfo=jst
      )
    elif result2:
      date_start = datetime.datetime(
        year=int(result2.group(1)),month=int(result2.group(2)),day=int(result2.group(3)),
        hour=0,minute=0,second=0,tzinfo=jst
      )
      date_end = datetime.datetime(
        year=int(result2.group(1)),month=int(result2.group(2)),day=int(result2.group(3)),
        hour=0,minute=0,second=0,tzinfo=jst
      )
    else:
      date_start = None
      date_end = None
    yield Post(url=response.meta['url'],time=time, title=title, date_start=date_start, date_end=date_end)

