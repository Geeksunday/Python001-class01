# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd
import os


dic_item = {'电影名称': [], '电影类型': [], '上映时间': []}
file_path = 'scrapy_XPath_猫眼电影前10.csv'


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        dic_item['电影名称'] = [item['name']]
        dic_item['电影类型'] = [item['mold']]
        dic_item['上映时间'] = [item['release_time']]

        if file_path not in os.listdir():
            pd.DataFrame(dic_item).to_csv(file_path,mode='a',index=False,encoding='utf-8-sig')
        else:
            pd.DataFrame(dic_item).to_csv(file_path,mode='a',index=False,header=False,encoding='utf-8-sig')
        return item
