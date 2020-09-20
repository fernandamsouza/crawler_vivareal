# Crawler Vivareal
> https://www.vivareal.com.br/

Dados extraídos de anúncios sobre a região de Florianópolis - SC - Brasil.

## Instalação (Linux)

#### 1. Primeiramente, instalação dos packages necessários para o crawler: 

```shell
pip install -r requirements.txt
```

#### 2. Aconselha-se o uso da IDLE PyCharm:

```shell
https://www.jetbrains.com/pt-br/pycharm/download/#section=windows
```
ou 
```shell
sudo snap install pycharm-community --classic
```

#### 3. Instalação ElasticSearch

```shell
https://www.elastic.co/pt/downloads/elasticsearch
```
ou 
```shell
sudo apt-get update && sudo apt-get install elasticsearch
```

#### 4. Instalação Kibana

```shell
sudo apt install kibana
sudo systemctl enable kibana
sudo systemctl start kibana
```

## Preparação do Ambiente

#### 1. Iniciação do ElasticSearch:

Navegue até a pasta de instação do ElasticSearch e execute:

```shell
./bin/elasticsearch
```
#### 1.2 Execução do cluster

```shell
curl 'http://localhost:9200/'
```
#### 2. Iniciação Kibana para visualização dos dados:

Navegue até a pasta de instalação do Kibana e execute:

```shell
bin/kibana
```

## Execução do Crawler

#### 1. Crawler

```shell
scrapy crawl vivareal
```

#### 2. Gravação em um arquivo .json

```shell
scrapy crawl vivareal -o vivareal.json
```

#### 3. Agora, para visualização dos dados dentro do indexador, acesse:

#### 3.1 ElasticSearch Puro

```shell
http://localhost:9200/vivareal/_search
```

#### 3.2 Interface Kibana

```shell
http://localhost:5601
```






