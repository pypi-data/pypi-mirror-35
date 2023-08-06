#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy import Spider, Request
import logging
import regex

class MCCMNC(CrawlSpider):
    name = 'mccmnc'
    start_urls = ['http://www.mcc-mnc.com']
    logging.info(start_urls)

    def parse(self, response):
        for no, tr in enumerate(response.css('tbody > tr')):
            for colno, col in enumerate(tr.css('td')):
                text = col.css('::text').extract()
                if len(text) > 0:
                    if colno == 0:
                        mcc = int(text[0])
                    elif colno == 1:
                        try:
                            mnc = int(text[0])
                        except:
                            mnc = None
                    elif colno == 2:
                        iso = text[0]
                    elif colno == 3:
                        country = text[0]
                    elif colno == 4:
                        country_code = text[0]
                    elif colno == 5:
                        network = text[0]
                        yield({'mcc': mcc, 'mnc': mnc, 'iso': iso, 'network': network, 'country': country, 'country_code': country_code})

