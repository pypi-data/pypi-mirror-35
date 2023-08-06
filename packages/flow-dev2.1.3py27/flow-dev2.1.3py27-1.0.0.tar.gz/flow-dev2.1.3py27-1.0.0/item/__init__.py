# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 下午7:32
# @Author  : Shark
# @File    : __init__.py.py
import scrapy

class ShipinItem(scrapy.Item):

    thumb_img = scrapy.Field()  ##缩略图
    update_status = scrapy.Field()  ##更新状态
    title = scrapy.Field()  ##标题
    role_info = scrapy.Field()  ##演员信息
    info_href = scrapy.Field()  ##详情链接
    category = scrapy.Field()  ##类别
    info = scrapy.Field()  ##简介
    area = scrapy.Field()  ##地区
    language = scrapy.Field()  ##语言
    update_time = scrapy.Field()  ##更新时间
    station = scrapy.Field()  ##电视台
    type = scrapy.Field()  ##类型
    play_time = scrapy.Field()  ##播放时间
    number = scrapy.Field()  ##播放集数
    current_number = scrapy.Field()  ##当前集数
    current_title = scrapy.Field()  ##当前标题
    play_href = scrapy.Field()  ##播放页链接
    play_thumb = scrapy.Field()  ##播放缩略图
    play_counts = scrapy.Field()  ##播放次数
    score = scrapy.Field()  ##评分

    flow_id = scrapy.Field()  ##业务id
    join_id = scrapy.Field()  ##关联id
    update_time = scrapy.Field()  ##抓取时间戳

