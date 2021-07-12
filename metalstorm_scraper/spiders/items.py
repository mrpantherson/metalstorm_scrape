# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Band(scrapy.Item):
    rank = scrapy.Field()
    name = scrapy.Field()
    genre = scrapy.Field()
    country = scrapy.Field()
    formed = scrapy.Field()
    split = scrapy.Field()
    fans = scrapy.Field()
    band_link = scrapy.Field()
    img_link = scrapy.Field()
