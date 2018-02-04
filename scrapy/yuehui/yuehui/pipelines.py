# -*- c oding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class YuehuiPipeline(object):
    def __init__(self):
        self.filename = open("yuehui.json","w")
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False)
        self.filename.write(content.encode("utf-8"))
        return item

    def close_spider(self,spider):
        self.filename.close()
