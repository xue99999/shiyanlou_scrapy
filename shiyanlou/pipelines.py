# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from shiyanlou.models import Course, engine, User
from shiyanlou.items import CourseItem, UserItem


class ShiyanlouPipeline(object):
    def process_item(self, item, spider):

        if isinstance(item, CourseItem):
            self._process_course_item(item)
        else:
            self._process_user_item(item)

        return item

    def _process_course_item(self, item):
        item['students'] = int(item['students'])
        
#        self.session.add(Course(**item))

        if item['students'] < 1000:
            raise DropItem('Course students less than 1000')
        else:
            self.session.add(Course(**item))


    def _process_user_item(self, item):
        
        item['level'] = int(item['level'][1:])

        item['join_date'] = datetime.strptime(item['join_date'].split()[0], '%Y-%m-%d').date()
        item['learn_courses_num'] = int(item['learn_courses_num'])

        self.session.add(User(**item))
        


    def open_spider(self, spider):

        Session = sessionmaker(bind=engine)
        self.session = Session()


    def close_spider(self, spider):

        self.session.commit()
        self.session.close()
