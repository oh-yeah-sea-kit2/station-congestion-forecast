# -*- coding: utf-8 -*-
import scrapy
from ..items import Post
import urllib.parse

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
    yield Post(url=response.meta['url'],time=time, title=title, date=date)

