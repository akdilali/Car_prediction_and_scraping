import scrapy
from ..items import ScrapyCarsItem
from scrapy import Request
from urllib.parse import urlparse
from urllib.parse import urljoin


class CarSpider(scrapy.Spider):
    name = 'Car'
    #allowed_domains = ['https://www.tasit.com/otomobil']
    # start_urls = ['https://www.tasit.com/otomobil/']
    start_urls=['https://www.tasit.com/otomobil/acura',
                'https://www.tasit.com/otomobil/alfa-romeo',
                'https://www.tasit.com/otomobil/aston-martin',
                'https://www.tasit.com/otomobil/audi',
                'https://www.tasit.com/otomobil/bmw',
                'https://www.tasit.com/otomobil/bentley',
                'https://www.tasit.com/otomobil/cadillac',
                'https://www.tasit.com/otomobil/chery',
                'https://www.tasit.com/otomobil/chevrolet',
                'https://www.tasit.com/otomobil/citroen',
                'https://www.tasit.com/otomobil/chrysler',
                'https://www.tasit.com/otomobil/dacia',
                'https://www.tasit.com/otomobil/dodge',
                'https://www.tasit.com/otomobil/ferrari',
                'https://www.tasit.com/otomobil/fiat',
                'https://www.tasit.com/otomobil/ford',
                'https://www.tasit.com/otomobil/honda',
                'https://www.tasit.com/otomobil/hyundai',
                'https://www.tasit.com/otomobil/isuzu',
                'https://www.tasit.com/otomobil/jaguar',
                'https://www.tasit.com/otomobil/jeep',
                'https://www.tasit.com/otomobil/kia',
                'https://www.tasit.com/otomobil/lada',
                'https://www.tasit.com/otomobil/lamborghini',
                'https://www.tasit.com/otomobil/land-rover',
                'https://www.tasit.com/otomobil/maserati',
                'https://www.tasit.com/otomobil/mazda',
                'https://www.tasit.com/otomobil/mclaren',
                'https://www.tasit.com/otomobil/mercedes',
                'https://www.tasit.com/otomobil/mini',
                'https://www.tasit.com/otomobil/mitsubishi',
                'https://www.tasit.com/otomobil/nissan',
                'https://www.tasit.com/otomobil/opel',
                'https://www.tasit.com/otomobil/peugeot',
                'https://www.tasit.com/otomobil/porsche',
                'https://www.tasit.com/otomobil/renault',
                'https://www.tasit.com/otomobil/skoda',
                'https://www.tasit.com/otomobil/seat',
                'https://www.tasit.com/otomobil/smart',
                'https://www.tasit.com/otomobil/ssangyong',
                'https://www.tasit.com/otomobil/subaru',
                'https://www.tasit.com/otomobil/suzuki',
                'https://www.tasit.com/otomobil/tata',
                'https://www.tasit.com/otomobil/tofas',
                'https://www.tasit.com/otomobil/toyota',
                'https://www.tasit.com/otomobil/volkswagen',
                'https://www.tasit.com/otomobil/volvo',
                'https://www.tasit.com/otomobil/diger'
                ]

    def parse(self, response):
        for href in response.css('.title.vertical-overflow.offer-link::attr(href)').extract():
            url = response.urljoin(href)
            print(type(url))
            print(url)
            yield scrapy.Request(url, callback = self.parse_page)

        next_page =  response.css('.btn.next::attr(href)')[1].extract()
        next_page = f"https://www.tasit.com{next_page}"
        print(next_page)
        if next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_link, callback = self.parse)


    def parse_page(self,response):
        item = ScrapyCarsItem()
        Brand = response.css('.offer-info-item').css("span::text")[5].extract()
        Model = response.css('.offer-info-item').css("span::text")[7].extract()
        Title = response.css('.offer-detail-title::text').extract()
        Price = response.css('.offer-price::text').extract()
        Model_year = response.css('.offer-info-item').css("span::text")[11].extract()
        Variant = response.css('.offer-info-item').css("span::text")[9].extract()
        Kilometer = response.css('.offer-info-item').css("span::text")[13].extract()
        Fuel_type = response.css('.offer-info-item').css("span::text")[15].extract()
        Gear_type = response.css('.offer-info-item').css("span::text")[17].extract()
        Engine_power = response.css('.offer-info-item').css("span::text")[21].extract()
        Engine_capacity = response.css('.offer-info-item').css("span::text")[19].extract() 
        From_who = response.css('.offer-info-item').css("span::text")[23].extract()
        District = response.css('.offer-district-container::text').extract()
        Date = response.css('.offer-info-item').css("span::text")[3].extract()


        item["Brand"] = Brand
        item["Model"] = Model
        item["Title"] = Title
        item["Price"] = Price 
        item["Model_year"] = Model_year 
        item["Variant"] = Variant
        item["Kilometer"] = Kilometer
        item["Fuel_type"] = Fuel_type 
        item["Gear_type"] = Gear_type
        item["Engine_power"] = Engine_power 
        item["Engine_capacity"] = Engine_capacity
        item["From_who"] = From_who 
        item["District"] = District
        item["Date"] = Date

        yield item 
    