import scrapy
from scrapy.selector import Selector

class Spider1Spider(scrapy.Spider):
    name = 'coronavirus'
    allowed_domains = ['www.americanas.com.br']
    start_urls = ['https://www.americanas.com.br/produto/4265732670?pfm_carac=computer&pfm_page=search&pfm_pos=grid&pfm_type=search_page&offerId=61827372d9fd6edeec2cd26f']
def parse(self, response):
         seller=response.xpath("//div[@class='offers-box__Wrapper-sc-189v1x3-0 kegaFO']//font[@style='vertical-align: inherit;'])[3]//text()").get()
         discription=response.xpath("(//div[@class='offers-box__Wrapper-sc-189v1x3-0 kegaFO']/p/a/@href)[1]").get()

        #  for product,p in zip(seller,price):
        #   name=product.xpath(".//text()").get()
        #   price=p.xpath(".//text()").get()
        #   link=product.xpath("//div[@class='inStockCard__Wrapper-sc-1ngt5zo-0 iRvjrG']/a/@href").get()
         yield{
            "seller":seller,
            # "Countrylink":link
            "description":discription
          }