import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' # Heredado

    allowed_domains = [ # Heredado
        'un.org'
    ]

    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    regla_uno = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' # Nombre funcion a ejecutar para parsear 
        ),
        # segundo parametro vacio
    )

    

    segmentos_url_permitidos = (
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ), callback='parse_page'
        ),
        # Parametro Vacio
    )

    rules = regla_dos # Heredada

    def parse_page(self, response):
        lista_programas = response.css('div.field-items > div.field-item > h4::text').extract()
        for agencia in lista_programas:
            with open('onu_agencias.txt', 'a+', encoding = 'utf-8') as archivo:
                archivo.write(agencia + '\n')



