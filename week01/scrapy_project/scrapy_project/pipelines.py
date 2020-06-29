# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import os

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        result_data = pd.DataFrame(dict(item), index=[0])
        if os.path.exists('./scrapy_result.csv'):
            header = False
        else:
            header = True
        result_data.to_csv('./scrapy_result.csv', mode='a', index=False, header=header)
        return item