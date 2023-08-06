#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy import Spider, Request
import logging
import regex

class MCCMNC(CrawlSpider):
    name = 'mccmnc'
    start_urls = ['http://mcclist.com/mobile-network-codes-country-codes.asp']
    logging.info(start_urls)

    def parse(self, response):
        countries = []
        for country in response.css('h3 > a ::text').extract():
            countries.append(country.replace('Afganistan', 'Afghanistan'))
        for no, table in enumerate(response.css('table')):
            if no == 0:
                continue
            for row in table.css('tr'):
                text = row.css('td')
                for colno, col in enumerate(text.css('td ::text').extract()):
                    if colno == 0:
                        mcc = int(col)
                    elif colno == 1:
                        mnc = int(regex.sub(r'[^\d]', '', col))
                    elif colno == 2:
                        network = col
                    elif colno == 3:
                        operator = col
                    elif colno == 4:
                        active = col == 'Operational'
                        yield({'mcc': mcc, 'mnc': mnc, 'network': network, 'operator': operator, 'country': countries[no], 'active': active})

