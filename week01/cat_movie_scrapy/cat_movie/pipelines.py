# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CatMoviePipeline:
    file = None
    index = 0

    def open_spider(self, spider):
        self.file = open('movie.csv', 'a', encoding='utf-8')
        return self.file

    def process_item(self, item, spider):
        if self.index == 0:
            column_name = "电影名称,上映时间,类型\n"
            self.file.write(column_name)
            self.index = 1
        home_str = item['name'] + ',' + item['rel'] + ',' + item['type'] + '\n'
        self.file.write(home_str)

        return item

    def close_spider(self, spider):
        self.file.close()
