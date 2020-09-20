import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from crawler_vivareal.utils import get_random_agent
from crawler_vivareal.items import VivaRealItems
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

USER_AGENT = get_random_agent()


class crawlerVivarealSpider(CrawlSpider):
    name = 'vivareal'
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
    allowed_domains = ['www.vivareal.com.br']
    handle_httpstatus_list = [403,429]


    custom_settings = {
        'FEED_FORMAT':"csv",
        'FEED_URI':"vivareal.csv"
    }

    def __init__(self, *args, **kwargs):
        super(crawlerVivarealSpider, self).__init__(*args, **kwargs)
        self.main = 'https://www.vivareal.com.br'
        self.links = []
        self.driver = webdriver.Firefox()
        self.totalpages = 5
        self.contador = 0

    def start_requests(self):
        url = self.main + '/aluguel/santa-catarina/florianopolis/'
        yield scrapy.Request(url = url, callback = self.parse_page)

    def storeLinks(self, links):
        for link in links:
            self.links.append(link.get_attribute('href'))

    def parse_page(self, response):
        self.driver.get(response.url)
        while self.contador < self.totalpages:
            try:
                next = WebDriverWait(self.driver, 10)
                links = self.driver.find_elements_by_xpath(
                    '//a[@class="property-card__main-link js-carousel-link"]')
                self.storeLinks(links)
                next.until(EC.element_to_be_clickable(
                    (By.XPATH, '//a[@title="Próxima página"]'))).click()
                sleep(3)
                self.contador+=1
            except Exception:
                print('It has ended')
                #break
        self.driver.close()
        for item in self.links:
            yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        link = response.url.split('id-')[1]
        id = link.split('/')[0]
        link = response.url
        pagina = 'Vivareal'
        aluguel = response.xpath("//html/body/main/div[2]/div[2]/div[1]/div/div[1]/h3/text()")[0].extract()
        endereco = response.xpath("//*[@id='js-site-main']/div[2]/div[1]/div[1]/section/div/div/p/text()").extract()
        metragem = response.xpath("//*[@id='js-site-main']/div[2]/div[1]/div[2]/ul/li[1]/span/text()").extract()
        num_quartos = response.xpath("//*[@id='js-site-main']/div[2]/div[1]/div[2]/ul/li[2]/span/text()").extract()
        num_vagas_garagem = response.xpath("//*[@id='js-site-main']/div[2]/div[1]/div[2]/ul/li[4]/span/text()").extract()
        condominio = response.xpath("//*[@id='js-site-main']/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/span[2]/text()").extract()
        iptu = response.xpath("//*[@id='js-site-main']/div[2]/div[2]/div[1]/div/div[2]/ul/li[3]/span[2]/text()").extract()
        titulo_anuncio = response.xpath("//*[@id='js-site-main']/div[2]/div[1]/div[1]/section/div/h1/text()").extract()

        novo_item = VivaRealItems(pagina = pagina, id=id, link=link, titulo_anuncio = titulo_anuncio, aluguel = aluguel, endereco = endereco, metragem = metragem,
                                  num_quartos = num_quartos, num_vagas_garagem = num_vagas_garagem, condominio = condominio, iptu = iptu)
        yield novo_item


