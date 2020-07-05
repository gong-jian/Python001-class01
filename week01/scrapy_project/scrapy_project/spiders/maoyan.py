# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_project.items import ScrapyProjectItem
import os


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset=0']
    
   

    def start_request(self):
        # self.movie_num = self.settings.get('MOVIE_NUM')
        # print(self.movie_num)
        # page_num = (self.movie_num - 1)//30
        # for i in range(page_num + 1):
        #     url = f'https://maoyan.com/films?showType=3&offset={i * 30}'
        #     yield scrapy.Request(url=url, meta={'currentpage': i}, callback=self.parse)
        #问题:下面读取meta不对
        url = 'https://maoyan.com/films?showType=3&offset=0'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
        
        
    # 解析函数
    def parse(self, response):
        # print('测试数据：' + str(response.meta))
        # current_page = response.meta['currentpage']
        # self.movie_num = self.settings.get('MOVIE_NUM')
        # current_page_num = self.movie_num - current_page * 30
        selector_info = Selector(response=response)
        item = ScrapyProjectItem()
        for i, tags in enumerate(selector_info.xpath('//div[@class="movie-hover-info"]')):
            if i >= 10:     #读取10个电影，本想用current_page_num但有问题还未解决
                break
            for tag in tags.xpath('./div'):
                movie_name = tag.xpath('./@title').extract_first()
                print(movie_name)
                div_text = tag.xpath('./text()').extract()
                span_text = tag.xpath('./span/text()').extract_first()
                if span_text == '类型:':
                    movie_type = div_text[1].strip()
                    print(movie_type)
                if span_text == '上映时间:':
                    movie_time = div_text[1].strip()
                    print(movie_time)
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_time'] = movie_time
            yield item
