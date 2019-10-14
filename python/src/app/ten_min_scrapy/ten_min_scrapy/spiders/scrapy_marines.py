# -*- coding: utf-8 -*-
import scrapy
from ..items import Post
import datetime
import urllib.parse

class ScrapyMarinesSpider(scrapy.Spider):
  name = 'scrapy_marines'
  allowed_domains = ['www.marines.co.jp']
  start_urls = ['http://www.marines.co.jp/game/schedule/index.html']

  def parse(self, response):
    for post in response.css('div.pl_blockB01 > table > tbody > tr'):
      # 欲しいデータ
      # 日付、球場、URL
      # ZOZOマリンの球場データのみ格納
      place = post.css('td.pl_tCenter::text').extract_first().strip()
      if place != 'ZOZOマリン':
        continue
      title = ""
      url = post.css('td > div.pl_vs > div > p.pl_Run > a::attr(href)').extract_first().strip()
      url = urllib.parse.urljoin(self.allowed_domains[0], url)
      time = ""
      date = post.css('td > div.pl_date > p > nobr::text').extract_first().strip()

      jst = datetime.timezone(datetime.timedelta(hours=9))
      date_start = datetime.datetime(
        year=datetime.date.today().year,month=datetime.date.today().month,day=int(date),
        hour=0,minute=0,second=0,tzinfo=jst
      )
      date_end = datetime.datetime(
        year=datetime.date.today().year,month=datetime.date.today().month,day=int(date),
        hour=0,minute=0,second=0,tzinfo=jst
      )
      yield Post(
        url=url,
        time=time, 
        title=title, 
        date_start=date_start, 
        date_end=date_end
      )
