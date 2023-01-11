# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class CategoryPipeline:
    def __init__(self):
        self.file = open('categories.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['name', 'link'])

    def close_spider(self, spider):
        if spider.name == 'category_spider':
            self.file.close()

    def process_item(self, item, spider):
        if spider.name == 'category_spider':
            self.writer.writerow([item['name'], item['link']])
            return item


class RestaurantPipeline:
    def __init__(self):
        self.file = open('restaurants.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['name', 'deliver_time', 'deliver_fee', 'rating', 'status'])

    def close_spider(self, spider):
        if spider.name == 'restaurant_spider':
            self.file.close()

    def process_item(self, item, spider):
        if spider.name == 'restaurant_spider':
            self.writer.writerow([item['name'], item['deliver_time'], item['deliver_fee'], item['rating'], item['status']])
            return item
