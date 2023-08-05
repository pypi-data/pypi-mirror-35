# -*- coding: utf-8 -*-
# !/usr/bin/python
# Create Date 2017/9/29 0029
import os
import json
import xlrd
import csv
__author__ = 'huohuo'
base_dir = os.path.dirname(__file__)
if __name__ == "__main__":
    pass


class File:

    def __init__(self):
        self.__description__ = '文件相关， 包括读文件，写文件， 下载文件'

    def read(self, file_name, sheet_name='', read_type='r', dict_name='', to_json=True, **kwargs):
        if os.path.exists(dict_name + "/" + file_name):
            url = dict_name + "/" + file_name
        else:
            url = base_dir + "/" + dict_name + "/" + file_name
        file_type = file_name.split('.')[-1]
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(url)
            return data.sheet_by_name(sheet_name)
        f = open(url, read_type)
        if file_type in ['csv', 'tsv'] or 'sep' in kwargs:
            sep = ',' if file_type == 'csv' else '\t'
            if 'sep' in kwargs:
                sep = kwargs['sep']
            delimiter = {'delimiter': sep}
            csv.register_dialect('my_dialect', **delimiter)
            cons = csv.reader(f, 'my_dialect')
            items = []
            keys = next(cons)
            for c in cons:
                if to_json:
                    item = {}
                    for i in range(len(keys)):
                        item[keys[i]] = c[i]
                    items.append(item)
                else:
                    items.append(c)
            csv.unregister_dialect('my_dialect')
            f.close()
            return items
        else:

            text = f.read()
            f.close()
        if file_type == 'json':
            return json.loads(text)
        return text

    def read_message(self, file_name, file_type='json', sheet_name='', read_type='r', developer='huohuo', message='success'):
        error_message = u'【开发者】：%s\n' % developer
        error_message += u'【文件类型】：%s\n' % file_type
        if file_type in ['xlsx', 'xls']:
            error_message += u'【sheet_name】：%s\n' % sheet_name
        error_message += u'【消息】：%s\n' % message
        error_message += u'【文件名】：\n%s\n' % file_name

    def write(self, file_name, data):
        file_type = file_name.split('.')[-1]
        postfix = file_type
        if file_name[-len(file_type):] == file_type:
            file_name = file_name[:len(file_name)-len(file_type)-1]
        url = "%s/%s.%s" % (base_dir, file_name, postfix)
        f = open(url, "w")
        if file_type == 'json':
            f.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))
        else:
            f.write(data)
        f.close()

    def download(self, pkg_parts, file_name):
        temp_data = self.read("demo.xml")
        temp_data = temp_data.replace('<pkg:part id="pkg_parts"></pkg:part>', pkg_parts)
        self.write(file_name, temp_data)
