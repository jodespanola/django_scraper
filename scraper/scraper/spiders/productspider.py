import scrapy


class ProductspiderSpider(scrapy.Spider):
    name = "productspider"
    allowed_domains = ["www.ebay.com"]
    start_urls = ["https://www.ebay.com/b/Athletic-Shoes/15709?US%2520Shoe%2520Size=10%7C10%252E5&US%2520Shoe%2520Size%2520%2528Men%2527s%2529=6%7C6%252E5&rt=nc&mag=1&_udlo=100"]

    def parse(self, response):
        products = response.css('li.s-item')

        for product in products:
            yield{
                'name' : product.css('h3.s-item__title ::text').get(),
                'price': product.css('span.s-item__price ::text').get(),
                'url': product.css('div.s-item__info a::attr(href)').get(),
                'image_url': product.css('img.s-item__image-img ::attr(src)').get()
            }

        next_page =  response.css('a.pagination__next ::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)