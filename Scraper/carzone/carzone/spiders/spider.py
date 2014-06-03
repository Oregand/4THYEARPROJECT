from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from carzone.items import CarzoneItem
from scrapy.settings import Settings




# from carzone.items import CarzoneItem


class ScrapyDemoSpider(CrawlSpider):
    name = "car4"
    allowed_domains = ["carzone.ie"]
    start_urls = [
"http://www.carzone.ie/search/results?nParam=4294911133%2B200590&searchsource=browse&cacheBuster=1401792077845644"]
    rules = (Rule(SgmlLinkExtractor(allow=('\\&page=\\d')), 'parse_start_url', follow=True),)


    def __init__(self, name=None, **kwargs):
        super(ScrapyDemoSpider, self).__init__(name, **kwargs)

    def parse_start_url(self, response):

        #Start at beginning of listings and get advert link
        hxs = HtmlXPathSelector(response)
        listings = hxs.select("//div[@class='vehicle-description']")
        links = []

        #Extract the link and add it to the array of links for current page
        for listing in listings:
            link = listing.select("div[@class='vehicle-make-model']/h3/a/@href").extract()[0]
            links.append(link)

        #use listing url to get content of the listing page
        for link in links:
            item = CarzoneItem()
            item['link'] = link

        #Finally, return the link as a meta object and call our second scraping function for futher details
        for link in links:
            yield Request(link, meta={'item': item}, callback=self.parse_listing_page)



            # return None

            #scrap listing page to get content

    def parse_listing_page(self, response):

        hxs = HtmlXPathSelector(response)


        #print "CALL BACK" - Testing

        item = response.request.meta['item']
        item['title'] = hxs.select('//*[@id="car-header"]/h1/text()').extract()[0].strip()
        item['link'] = response.url
        item['price'] = hxs.select('//*[@id="advertDetailsPrice"]/text()').extract()[0].strip()
        item['carYear'] = hxs.select('//*[@id="advertDetailsYear"]/text()').extract()[0].strip()
        item['location'] = hxs.select('//*[@id="advertDetailsLocation"]/text()').extract()[0].strip()
        item['mileage'] = hxs.select('//*[@id="advertDetailsMileage"]/text()').extract()[0].strip()
        item['engine'] = hxs.select('//*[@id="advertDetailsEngine"]/text()').extract()[0].strip()
        item['Transmission'] = hxs.select('//*[@id="advertDetailsTransmission"]/text()').extract()[0].strip()
        item['Colour'] = hxs.select('//*[@id="advertDetailsColour"]/text()').extract()[0].strip()
        item['Owners'] = hxs.select('//*[@id="advertDetailsOwners"]/text()').extract()[0].strip()
        item['NCT'] = hxs.select('//*[@id="advertDetailsNCTExpiry"]/text()').extract()[0].strip()
        item['BodyType'] = hxs.select('//*[@id="advertDetailsBodyType"]/text()').extract()[0].strip()

        yield item

    # class HasHeaderContract(Contract):
    #     URL = 'http://www.carzone.ie/search/Audi/A4/2.0TDI-1/49614000719014160/advert?channel=CARS'
    #
    #     def pre_process(self, response):
    #         for URL in self.args:
    #             if URL not in response.url:
    #                 raise ContractFail('URL not present')

