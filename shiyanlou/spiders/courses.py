# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'

    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        urls = (url_tmpl.format(i) for i in range(1, 23))
        return urls

    def parse(self, response):
        for course in reponse.css('div.course-body'):
            item = CourseItem({
                'name': course.css('div.course-name::text').extract_first(),
                'desc': course.css('div.course-desc::text').extract_first(),
                'type': course.css('div.course-footer span.pull-right::text').extract_first(),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
                })
            yield item
