# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.exporter import CsvItemExporter


class EdulinePipeline(object):
    def process_item(self, item, spider):
        return item


class SpecialityPipeline(object):

    def __init__(self):
        fields = ['college_name', 'province', 'examiee_type', 'year', 'speciality_name',
                  'avarage_score', 'high_score', 'low_score', 'batch_type']
        self.f = file('items.csv', 'a+b')
        self.exporter = CsvItemExporter(self.f, fields_to_export=fields)

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def spider_opened(self, spider):
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.f.close()