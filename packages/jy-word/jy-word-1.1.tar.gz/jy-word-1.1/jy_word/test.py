#! /usr/bin/env python
# coding: utf-8
__author__ = 'huo'
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

from jy_word.File import File
from jy_word.Word import Paragraph, Run, Set_page, Table, Tc, Tr, HyperLink
from Word import write_pkg_parts, get_imgs
img_info_path = 'img_info.json'

my_file = File()

r = Run(img_info_path)
hyperlink = HyperLink()
r.family_en = 'Times New Roman'
p = Paragraph()
set_page = Set_page().set_page
table = Table()
tr = Tr()
tc = Tc()

# 初号=42磅
# 小初=36磅
# 一号=26磅
# 小一=24磅
# 二号=22磅
# 小二=18磅
# 三号=16磅
# 小三=15磅
# 四号=14磅
# 小四=12磅
# 五号=10.5磅
# 小五=9磅
# 六号=7.5磅
# 小六=6.5磅
# 七号=5.5磅
# 八号=5磅


# ##################下载报告所需方法######################

def generate_word():
    file_name = 'my_word.doc'
    print u'%s begin.' % file_name
    imgs = get_imgs(os.path.dirname(__file__))
    my_file.write(img_info_path, imgs)
    body = p.h4('hello, my word!')
    body += p.write(r.picture(cx=10, rId='ex'))
    pkg = write_pkg_parts(imgs, body, title=[])
    my_file.download(pkg, file_name)
    print u'%s over.' % file_name


if __name__ == '__main__':
    generate_word()
