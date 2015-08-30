from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy
import re
import urlparse
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.settings import Settings
#import scrapy.http.Request

class TorrentItem(scrapy.Item):
    url = scrapy.Field()
    candidate = scrapy.Field()

class MaidsSpider(BaseSpider):
    name = 'woru'
    allowed_domains = ['isidewith.com']
    #start_urls = ['http://www.isidewith.com/elections/2016-presidential/%s' % page for page in xrange(1291201438, 1291201440)]
    start_urls = ['http://www.isidewith.com/elections/2016-presidential/%s' % page for page in xrange(1000000000,1000010000)]

    def parse(self, response):
        torrent = TorrentItem()
        if ("notice" not in str(response.url)) and ("status" not in str(response.url)):
            torrent['url'] = response.url
            #torrent['candidate'] = (str(response.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/h1/text()").extract()).split("with")[1]).split("on")[0]

        return torrent
