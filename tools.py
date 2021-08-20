import requests, json, urllib.parse
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.base_url = self.url.rsplit('/', 1)[0]

    def scrapePage(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")

        list = soup.find("div", class_="seznam")

        ids = [int(id['title']) for id in list.find_all("a", {"itemprop":"url"})]
        links = [urllib.parse.urljoin(self.base_url, link['href']) for link in list.find_all("a", {"itemprop":"url"})]
        titles = [title.text for title in list.find_all("span", {"class":"title"})]
        years = [int(year.find("strong").text) for year in list.find_all("span", {"class":"atribut leto"})]
        sizes = [float(size.text.replace(" m2","").replace(",",".")) for size in list.find_all("span", {"class":"velikost"})]
        prices = [float(price.text.replace(" €/mesec","").replace(".","").replace(",",".").replace(" €","")) for price in list.find_all("span", {"class":"cena"})]
        agencies = [agency.text for agency in list.find_all("span", {"class":"agencija"})]

        #data = {int(id['title']):{"Title":title.text, "Size":float(size.text.replace(" m2","").replace(",",".")), "Price":float(price.text.replace(" €/mesec","").replace(".","").replace(",",".")), "Year":year.text} for id, title, size, price, year in zip(ids, titles, sizes, prices, years)}

        print(links)