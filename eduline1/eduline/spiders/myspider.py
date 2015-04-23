#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'holmes'

import os
import sys
import string
import json
import scrapy
from eduline.items import SpecialityItem


class MySpider(scrapy.Spider):
    name = 'gkcx.eol.cn'
    start_urls = ['http://gkcx.eol.cn/schoolhtm/specialty/31/10034/specialtyScoreDetail_2010_10003.htm']

    __province_dict = {
        "安徽": "10008", "澳门": "10145", "北京": "10003", "重庆": "10028", "福建": "10024", "甘肃": "10023",
        "贵州": "10026", "广东": "10011", "广西": "10012", "河北": "10016", "河南": "10017", "黑龙江": "10031",
        "湖北": "10021", "湖南": "10022", "海南": "10019", "江苏": "10014", "江西": "10015", "吉林": "10004",
        "辽宁": "10027", "内蒙古": "10002", "宁夏": "10007", "青海": "10030", "上海": "10000", "山东": "10009",
        "山西": "10010", "陕西": "10029", "四川": "10005", "天津": "10006", "新疆": "10013", "西藏": "10025",
        "香港": "10020", "云南": "10001", "台湾": "10146", "浙江": "10018"
    }

    __examiee_dict = {
        "文科": "10034", "理科": "10035", "综合": "10090", "艺术类": "10091", "体育类": "10093"
    }

    __years_list = [
        "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007"
    ]

    def __init__(self):
        super(MySpider, self).__init__()
        self.__school_dict = self.__get_school_dict()

    def __get_school_dict(self):
        # TODO:(tian chen) change the hard code here!!
        p = os.path.abspath(os.path.dirname(__file__))
        temp = os.path.dirname(p)
        path = os.path.join(temp, os.path.join('resource','schools.json'))
        with file(path, 'r') as f:
            return json.load(f, encoding='utf-8')

    def parse(self, response):
        for school_id in self.__school_dict.keys():
            for province in self.__province_dict.keys():
                for examiee in self.__examiee_dict.keys():
                    for year in self.__years_list:
                        school = self.__school_dict[school_id]
                        province_id = self.__province_dict[province]
                        examiee_id = self.__examiee_dict[examiee]
                        url = 'http://gkcx.eol.cn/schoolhtm/specialty/{}/{}/specialtyScoreDetail_{}_{}.htm'.format(school_id,examiee_id,year,province_id)
                        yield scrapy.Request(url, callback=self.parse_detial, meta={'more':[school,province]})

    def parse_detial(self, response):
        for tr in response.xpath("//table[@name='tableList']/tr[position()>1]"):
            item = SpecialityItem()
            tr_content = tr.xpath("td/text()").extract()
            if len(tr_content) < 7:
                continue
            item['college_name'] = response.meta['more'][0]
            item['province'] = response.meta['more'][1]
            item['speciality_name'] = tr_content[0]
            item['year'] = tr_content[1]
            item['avarage_score'] = tr_content[2]
            item['high_score'] = tr_content[3]
            item['low_score'] = tr_content[4]
            item['examiee_type'] = string.strip(tr_content[5])
            item['batch_type'] = string.strip(tr_content[6])
            yield item
