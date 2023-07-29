import scrapy
from scraper.scraper.items import ProductItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst

class ProductspiderSpider(CrawlSpider):
    name = "productspider"
    allowed_domains = ["www.ebay.com"]
    start_urls = ["https://www.ebay.com/b/Athletic-Shoes/15709?US%2520Shoe%2520Size=10%7C10%252E5&US%2520Shoe%2520Size%2520%2528Men%2527s%2529=6%7C6%252E5&rt=nc&mag=1&_udlo=100"]

    rules = (
        Rule(
            LinkExtractor(allow=("pgn=")),
            callback="parse_property",
            follow=True,
        ),
    )

    def parse_property(self, response):
        

        products = response.css('li.s-item')

        for product in products:
            item = ProductItem()
            item['name'] = product.css('h3.s-item__title ::text').get()
            item['price'] = product.css('span.s-item__price ::text').get()
            item['url'] = product.css('div.s-item__info a::attr(href)').get()
            item['image_url'] = product.css('img.s-item__image-img ::attr(src)').get()
            yield item
            # property_loader = ItemLoader(item=ProductItem(), response=product)
            # property_loader.default_output_processor = TakeFirst()
            # property_loader.add_css('name', 'h3.s-item__title ::text')
            # property_loader.add_css('price', 'span.s-item__price ::text')
            # property_loader.add_css('url', 'div.s-item__info a::attr(href)')
            # property_loader.add_css('image', 'img.s-item__image-img ::attr(src)')

            # yield property_loader.load_item()
        # next_page =  response.css('a.pagination__next ::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)