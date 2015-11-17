# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from myapp.models import Person

class MybotPipeline(object):
    def process_item(self, item, spider):
        obj = Person.objects.get_or_create(name=item['name'])
        return obj