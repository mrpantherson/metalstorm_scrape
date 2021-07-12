# -*- coding: utf-8 -*-
"""
    Custom Spider for scraping the site MetalStorm
    
    TODO instead of hard coding pages, follow links to next page
    TODO sort output
    TODO clean req.txt

    Usage: In terminal
        scrapy crawl metalspider -O file.csv

"""
import scrapy
from .items import Band

PAGE_START = 1 # inclusive
PAGE_END = 166 # exclusive


class MetalStormSpider(scrapy.Spider):
    name = "metalspider"

    def start_requests(self):

        urls = [f'http://www.metalstorm.net/bands/index.php?b_sortby=&b_where=&b_what=&page={i}' for i in range(PAGE_START, PAGE_END) ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body = response.css('.cbox')
        rows = body.css('tr')
        for row in rows[1:]:
            item = Band()
            cols = row.css('td')

            item['rank'] = cols[0].css('span::text').getall()

            item['name'] = cols[2].css('a::text').getall()

            res = cols[3].css('a::text').getall()
            res = [i.strip().lower() for i in res]
            item['genre'] = ', '.join(res)

            res = cols[4].css('td::text').getall()
            item['country'] = res[0].strip()

            res = cols[5].css('td::text').getall()
            item['formed'] = res[0].strip()

            res = cols[6].css('td::text').getall()
            item['split'] = res[0].strip()
            
            res = cols[7].css('td::text').getall()
            item['fans'] = res[0].strip()

            res = cols[2].css('a::attr(href)').getall()
            item['band_link'] = res[0].strip()
           
            res = cols[1].css('img::attr(src)').getall()
            item['img_link'] = res[0].strip()

            yield item
