#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'holmes'

import json


def parse_json():
    items = ['{']
    with file("queryschool.json",'r') as f:
        str_json = json.load(f)
        for item in str_json['school']:
            items.append('"%s": "%s", ' % (item['schoolid'], item['schoolname']))
    s_temp = items[-1].split(',')[0]
    del items[-1]
    items.append(s_temp)
    items.append('}')
    dic = ''.join(items)

    with file("schools.json", 'w') as wf:
        s = unicode(dic).encode('utf-8')
        wf.write(s)


def test():
    with file('schools.json','r') as f:
        print json.load(f)['31']
        #return json.load(f)

if __name__ == '__main__':
    parse_json()
    test()
