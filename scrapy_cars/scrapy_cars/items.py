# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCarsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Brand = scrapy.Field()
    Model = scrapy.Field()
    Title = scrapy.Field()
    Price = scrapy.Field()
    Model_year = scrapy.Field()
    Variant = scrapy.Field()
    Kilometer = scrapy.Field()
    Fuel_type = scrapy.Field()
    Gear_type = scrapy.Field()
    Engine_power = scrapy.Field()
    Engine_capacity = scrapy.Field()
    From_who = scrapy.Field()
    District = scrapy.Field()
    Date = scrapy.Field()
