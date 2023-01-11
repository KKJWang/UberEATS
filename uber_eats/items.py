# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CategoryItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()


class RestaurantItem(scrapy.Item):
    name = scrapy.Field()
    deliver_time = scrapy.Field()
    deliver_fee = scrapy.Field()
    rating = scrapy.Field()
    status = scrapy.Field()
