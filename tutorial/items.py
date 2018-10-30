# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    star = scrapy.Field()
    intro = scrapy.Field()
    link = scrapy.Field()
