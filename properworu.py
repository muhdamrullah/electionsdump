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



class TorrentItem(scrapy.Item):
    url = scrapy.Field()
    name_1 = scrapy.Field()
    name_2 = scrapy.Field()
    name_3 = scrapy.Field()
    name_4 = scrapy.Field()
    name_5 = scrapy.Field()
    name_6 = scrapy.Field()
    name_7 = scrapy.Field()
    name_8 = scrapy.Field()
    name_9 = scrapy.Field()
    name_10 = scrapy.Field()
    name_11 = scrapy.Field()
    name_12 = scrapy.Field()
    name_13 = scrapy.Field()
    name_14 = scrapy.Field()
    name_15 = scrapy.Field()
    name_16 = scrapy.Field()
    name_17 = scrapy.Field()
    name_18 = scrapy.Field()
    name_19 = scrapy.Field()
    issues_1 = scrapy.Field()
    issues_2 = scrapy.Field()
    issues_3 = scrapy.Field()
    issues_4 = scrapy.Field()
    issues_5 = scrapy.Field()
    issues_6 = scrapy.Field()
    issues_7 = scrapy.Field()
    issues_8 = scrapy.Field()
    issues_9 = scrapy.Field()
    issues_10 = scrapy.Field()
    issues_11 = scrapy.Field()
    issues_12 = scrapy.Field()
    issues_13 = scrapy.Field()
    issues_14 = scrapy.Field()
    issues_15 = scrapy.Field()
    issues_16 = scrapy.Field()
    issues_17 = scrapy.Field()
    issues_18 = scrapy.Field()
    issues_19 = scrapy.Field()
    percentage_1 = scrapy.Field()
    percentage_2 = scrapy.Field()
    percentage_3 = scrapy.Field()
    percentage_4 = scrapy.Field()
    percentage_5 = scrapy.Field()
    percentage_6 = scrapy.Field()
    percentage_7 = scrapy.Field()
    percentage_8 = scrapy.Field()
    percentage_9 = scrapy.Field()
    percentage_10 = scrapy.Field()
    percentage_11 = scrapy.Field()
    percentage_12 = scrapy.Field()
    percentage_13 = scrapy.Field()
    percentage_14 = scrapy.Field()
    percentage_15 = scrapy.Field()
    percentage_16 = scrapy.Field()
    percentage_17 = scrapy.Field()
    percentage_18 = scrapy.Field()
    percentage_19 = scrapy.Field()
    issname_1 = scrapy.Field()
    issname_2 = scrapy.Field()
    issname_3 = scrapy.Field()
    issname_4 = scrapy.Field()
    issname_5 = scrapy.Field()
    issname_6 = scrapy.Field()
    issname_7 = scrapy.Field()
    issname_8 = scrapy.Field()
    issname_9 = scrapy.Field()
    issimp_1 = scrapy.Field()
    issimp_2 = scrapy.Field()
    issimp_3 = scrapy.Field()
    issimp_4 = scrapy.Field()
    issimp_5 = scrapy.Field()
    issimp_6 = scrapy.Field()
    issimp_7 = scrapy.Field()
    issimp_8 = scrapy.Field()
    issimp_9 = scrapy.Field()
    isspeople_1 = scrapy.Field()
    isspeople_2 = scrapy.Field()
    isspeople_3 = scrapy.Field()
    isspeople_4 = scrapy.Field()
    isspeople_5 = scrapy.Field()
    isspeople_6 = scrapy.Field()
    isspeople_7 = scrapy.Field()
    isspeople_8 = scrapy.Field()
    isspeople_9 = scrapy.Field()
    #trythis = scrapy.Field()


class MaidsSpider(BaseSpider):
    name = 'woru'
    allowed_domains = ['isidewith.com']
    start_urls = ['http://www.isidewith.com/elections/2016-presidential/%s' % page for page in xrange(0, 10000)]

    def parse(self, response):
        torrent = TorrentItem()
        if ("notice" not in str(response.url)) and ("status" not in str(response.url)) and ("no-answers" not in str(response.url)) and ("no-traffic" not in str(response.url)):
            
            torrent['url'] = response.url

            for hindex in range (1, 10):
                torrent['issname_%s' % hindex] = ((response.xpath("//*[@id='resultsByIssue']/div/div[%s]/a/h5/text()" % hindex).extract()))
                torrent['issimp_%s' % hindex] = ((response.xpath("//*[@id='resultsByIssue']/div/div[%s]/a/p[1]/text()" % hindex).extract()))
                torrent['isspeople_%s' % hindex] = ((response.xpath("//*[@id='resultsByIssue']/div/div[%s]/a/p[2]/text()" % hindex).extract()))

            for index in range (1, 20):
                torrent['name_%s' % index] = ((response.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[%s]/a/h5/text()" % index).extract()))
                torrent['issues_%s' % index] = ((response.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[%s]/a/p[2]/text()" % index).extract()))
                torrent['percentage_%s' % index] = ((response.xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[%s]/a/p[1]/text()" % index).extract()))

        return torrent
