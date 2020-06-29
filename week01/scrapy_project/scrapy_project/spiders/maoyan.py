# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy_project.items import ScrapyProjectItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

    def start_request(self, response):
        self.movie_num = self.settings.get('MOVIE_NUM')
        print(self.movie_num)
        page_num = (self.movie_num - 1)//30
        for i in range(page_num + 1):
            url = 'https://maoyan.com/films?showType=3&offset={}'.format(i * 30)
            print(url)
            yield scrapy.Request(url=url, meta={'currentpage': i}, callback=self.parse)

    def parse(self, response):
        # print(response.meta['currentpage'])
        # current_page = response.meta['currentpage']
        current_page_num = self.movie_num - 0 * 30
        selector_info = Selector(response=response)
        for i, tags in enumerate(selector_info.xpath('//div[@class="movie-hover-info"]')):
            if i == current_page_num:
                break
            movie_name = None
            movie_type = None
            movie_time = None
            item = ScrapyProjectItem()
            for tag in tags.xpath('./div'):
                movie_name = tag.xpath('./@title').extract_first()
                span_text = tag.xpath('./span/text()').extract_first()
                if span_text == '类型:':
                    movie_type = tag.xpath('./text()').extract_first.strip()
                if span_text == '上映时间:':
                    movie_time = tag.xpath('./text()').extract_first.strip()
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_time'] = movie_time
            yield item
