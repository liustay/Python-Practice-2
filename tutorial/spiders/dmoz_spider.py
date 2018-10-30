import scrapy
from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["movie.douban.com"]
	start_urls = [
		"https://movie.douban.com/top250"
	]

	def parse(self, response):
		movie_list = response.xpath("//div[@class='article']/ol[@class='grid_view']/li")
		for item in movie_list:
			movie_item = TutorialItem()
			movie_item["number"] = item.xpath(".//div[@class='item']/div[@class='pic']/em/text()").extract_first()
			movie_item["title"] = item.xpath(".//div[@class='info']/div[@class='hd']/a/span[@class='title'][1]/text()").extract_first()
			content = item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()").extract()
			for i_content in content:
				movie_item["desc"] = "".join(i_content.split())
			movie_item["star"] = item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract_first()
			movie_item["intro"] = item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract_first()
			movie_item["link"] = item.xpath(".//div[@class='item']/div[@class='pic']/a/@href").extract_first()
			yield movie_item
			next_link = response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract()
			if next_link:
				next_link = next_link[0]
				yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback = self.parse)

