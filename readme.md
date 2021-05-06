# Readme 

I scraped data from website with python scrapy.
I made a price prediction after the cleaning and pre-processing stages.

#Install scrapy

pip install scrapy or conda install -c conda-forge scrapy

#Create a project

scrapy startproject example

#create a spider

scrapy genspider example2 https://www.website.com

#Run spider
scrapy crawl example2

scrapy crawl Spidername -o Output.json

the desired file type can be specified in the setting file

FEED_FORMAT = "csv"

FEED_URI = "Scraping.csv"

# Using scrapy shell 
Search with scrapy shell to find data

entry : scrapy shell or scrapy shell https://www.website.com

change the website : fetch("https://www.website.com")

open website : view(response)

use xpath or css selector to find data
response.css("._3a1XQ88S::text").extract() 
response.xpath('//p/strong/text()').extract()

print response.text (website source code)



# Machine learning model

After preprocessing random forest regressor is used.
After linear discriminant analysis accuracy rate increased.















