# -*- coding: utf-8 -*-
import scrapy


class BrandSpider(scrapy.Spider):
    name = "brand"
    allowed_domains = ["http://brandirectory.com/"]
    start_urls = ['http://brandirectory.com/league_tables/table/global-500-2014']

    def parse(self, response):
        name = response.css("td.leftalign a::text").extract()

        yield {
    	  "name": name
    	}
