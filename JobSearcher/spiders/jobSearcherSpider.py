# -*- coding: utf-8 -*-
import scrapy


class JobsearcherspiderSpider(scrapy.Spider):
    name = 'jonSearcherSpider'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/d/automotive-services/search/aos']

    def parse(self, response):

        # extract job urls from webpage
        listOfJobLinks = response.xpath('//li[@class="result-row"]')
        # extract all jobs details list one by one
        for jobLink in listOfJobLinks:
            date = jobLink.xpath('.//*[@class="result-date"]/@datetime').extract_first()
            link = jobLink.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
            text = jobLink.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()

            yield scrapy.Request(link,
                                 callback=self.parse_job_page,
                                 meta={'date': date,
                                       'link': link,
                                       'text': text})
        # extract next page url and get webpage
        next_page_url = response.xpath('//a[text()="next > "]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

    def parse_job_page(self, response):
        date = response.meta['date']
        link = response.meta['link']
        text = response.meta['text']
        # extract deails of specific search
        compensation = response.xpath('//*[@class="attrgroup"]/span[1]/b/text()').extract_first()
        type = response.xpath('//*[@class="attrgroup"]/span[2]/b/text()').extract_first()
        images = response.xpath('//*[@id="thumbs"]//@href').extract()
        address = response.xpath('//*[@id="postingbody"]/text()').extract()

        yield {'date': date,
               'link': link,
               'text': text,
               'compensation': compensation,
               'type': type,
               'images': images,
               'address': address}
