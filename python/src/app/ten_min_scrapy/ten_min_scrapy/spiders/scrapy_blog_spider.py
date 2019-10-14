# -*- coding: utf-8 -*-
import scrapy
from ..items import Post

class ScrapyBlogSpiderSpider(scrapy.Spider):
  name = 'scrapy_blog_spider'
  allowed_domains = ['blog.scrapinghub.com']
  start_urls = ['http://blog.scrapinghub.com/']

  def parse(self, response):
    for post in response.css('.post-listing .post-item'):
      yield Post(
        url=post.css('div.post-header a::attr(href)').extract_first().strip(),
        title=post.css('div.post-header a::text').extract_first().strip(),
        date=post.css('div.post-header span.date a::text').extract_first().strip(),
      )
    
    older_post_link = response.css('.blog-pagination a.next-posts-link::attr(href)').extract_first()
    if older_post_link is None:
      return
    
    older_post_link = response.urljoin(older_post_link)
    print(older_post_link)
    yield scrapy.Request(older_post_link, callback=self.parse)

