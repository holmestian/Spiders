# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EdulineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SpecialityItem(scrapy.Item):
    college_name = scrapy.Field()
    province = scrapy.Field()
    examiee_type = scrapy.Field()
    year = scrapy.Field()
    speciality_name = scrapy.Field()
    avarage_score = scrapy.Field()
    high_score = scrapy.Field()
    low_score = scrapy.Field()
    batch_type = scrapy.Field()