# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class VivaRealItems(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    link = scrapy.Field()
    titulo_anuncio = scrapy.Field()
    metragem = scrapy.Field()
    aluguel = scrapy.Field()
    endereco = scrapy.Field()
    condominio = scrapy.Field()
    num_quartos = scrapy.Field()
    num_vagas_garagem = scrapy.Field()
    iptu = scrapy.Field()
    pagina = scrapy.Field()
