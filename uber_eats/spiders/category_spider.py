import scrapy
import uber_eats.items


class CategorySpider(scrapy.Spider):
    name = "category_spider"
    start_urls = [
        "https://www.ubereats.com/category/cambridge-ma"
    ]
    custom_settings = {
        'ITEM_PIPELINES': { 'uber_eats.pipelines.CategoryPipeline': 300 }
    }

    def parse(self, response):
        for category_a in response.xpath('//*[@id="main-content"]/div/div[3]/a'):
            if category_a is not None:
                name = category_a.xpath('text()').get()
                link = category_a.xpath('@href').get()
                item = uber_eats.items.CategoryItem(name=name, link=link)
                yield item

    def parse(self, response):
        for category_a in response.xpath('//*[@id="main-content"]/div/div[3]/a'):
            if category_a is not None:
                category = category_a.xpath("@href").get()
                name = str(category).split('/')[-1]
                link = self.start_urls[0] + category
                item = uber_eats.items.CategoryItem(name=name, link=link)
                yield item


