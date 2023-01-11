import scrapy
import uber_eats.items


class RestaurantSpider(scrapy.Spider):
    name = "restaurant_spider"
    start_urls = [
        'https://www.ubereats.com/category/cambridge-ma/cantonese'
    ]
    custom_settings = {
        'ITEM_PIPELINES': { 'uber_eats.pipelines.RestaurantPipeline': 300 }
    }

    def parse(self, response):
        for restaurant_div in response.xpath('//*[@id="main-content"]/div[5]/div/div'):
            if restaurant_div is not None:
                name = restaurant_div.xpath('div/a/h3/text()').get()
                rating = restaurant_div.xpath('div/div/div/div/div[3]/text()').get()
                rating = rating if rating is not None else ""
                deliver_time = restaurant_div.xpath('div/div/div/div/div[1]/div/div[1]/div/span/text()').get()
                deliver_time = deliver_time if deliver_time is not None else ""
                deliver_fee = restaurant_div.xpath('div/div/div/div/div[1]/div/div[2]/div/span/text()').get()
                deliver_fee = deliver_fee if deliver_fee is not None else ""
                if deliver_fee != "":
                    deliver_fee = deliver_fee.split(' ')[0]
                status = restaurant_div.xpath('div/div/div/figure/figcaption/div/text()').get()
                status = "open" if status is None else "closed: " + status
                item = uber_eats.items.RestaurantItem(name=name, rating=rating,
                                                      deliver_time=deliver_time, deliver_fee=deliver_fee, status=status)
                yield item
