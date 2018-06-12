# spiders 一共4个， 需要单独执行
## users
> 用途: 爬取部分用户的个人信息

## courses
> 用途: 爬取所有课程的name, description, type, students

## courses_image
> 用途: 爬取所有课程的封面图并下载，
scrapy 内部内置了下载图片的 pipeline，
这个爬虫需要在setting.py中配置:
``` python
  # 要把ITEM_PIPELINES里面的其他pipeline注释掉， 我们不需要
  ITEM_PIPELINES = { 
    'scrapy.pipelines.images.ImagesPipeline': 100
  }
  # 图片保存的位置， 图片保存在full文件夹下
  IMAGES_STORE = 'images'
  
  # 图片保存在small文件夹下
  IMAGES_THUMBS = {
    'small': (50, 50)
  }
  
  # 图片要安装image
  sudo pip3 install image
  scrapy crawl courses_image
```
## multipage
> 用途：爬取课程的 name, imgSrc, author。 author信息在点进去的详情页

scrapy 的解决方案是多级 request 与 parse。简单的说就是先请求课程首页，
在回调函数 parse 中解析出课程名称和课程图片链接，
然后在 parse 函数再构造一个请求到课程详情页面，再在处理课程详情页的回调函数中解析出课程作者。

> 运行的时候， 需要把所有的pipeline注释掉， 因为我们没写到数据库
``` python
  scrapy crawl multipage -o data.json
```

