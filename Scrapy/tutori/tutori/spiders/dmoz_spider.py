import scrapy
from tutori.items import DmozItem

class DmozSpider(scrapy.Spider):
    name="dmoz"
    allowed_domans=["dmoztoos.net"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self,response):

        # for sel in response.xpath("//div[@id='site-list-content']"):
        for sel in response.xpath("//div[@class='title-and-desc']"):
            #title = sel.xpath('div/div').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('div/text()').extract()
            #print title, link, desc
            print link,desc



        # filename=response.url.split("/")[-2]
        # with open(filename,'wb') as f:
        #     f.write(response.body)