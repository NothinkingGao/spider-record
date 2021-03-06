#coding:utf-8
import scrapy

class BlogSpider(scrapy.Spider):
	name='blogspider'
	start_urls=['https://blog.scrapinghub.com']

	def parse(self,response):
		for title in response.css('h2.entry-title'):
			yield {'title':title.css('a::text').extract_first()}

		for next_page in response.css('div.prev-post>a'):
			yield response.follow(next_page,self.parse)

#运行方式
#scrapy runspider scrapy-record1.py
