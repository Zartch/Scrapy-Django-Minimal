# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from mybot.items import PersonItem


class ExampleSpider(BaseSpider):
    name = "example"
    allowed_domains = ["dmoz.org"]
    start_urls = ['http://www.dmoz.org/World/Espa%C3%B1ol/Artes/Artesan%C3%ADa/']

    def parse(self, response):
        # do stuff
        return PersonItem(name='zartch')