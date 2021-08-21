import requests, json, urllib.parse
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.base_url = self.url.rsplit('/', 1)[0]
        self.data = None

    def scrapePage(self):
        """
        Scrapes webpage for appartments and saves them to dictionary.
        """

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        list = soup.find("div", class_="seznam").find_all("div", {"class":"oglas_container"})

        for i in list:
            try:
                print(i.find("a")['title'])
                print(i.find("a").find("span", {"class":"title"}).text)
            except:
                print("nema")


        """

        ids = [int(id['title']) for id in list.find_all("a", {"itemprop":"url"})]
        links = [urllib.parse.urljoin(self.base_url, link['href']) for link in list.find_all("a", {"itemprop":"url"})]
        titles = [title.text for title in list.find_all("span", {"class":"title"})]
        years = [int(year.find("strong").text) for year in list.find_all("span", {"class":"atribut leto"})]
        sizes = [float(size.text.replace(" m2","").replace(",",".")) for size in list.find_all("span", {"class":"velikost"})]
        prices = [float(price.text.replace(" €/mesec","").replace(".","").replace(",",".").replace(" €","").replace("/osebo","")) for price in list.find_all("span", {"class":"cena"})]
        agencies = [agency.text for agency in list.find_all("span", {"class":"agencija"})]

        features = [ids, links, titles, years, sizes, prices, agencies]

        self.data = {id:{"Title":title, "Price":price, "Size":size, "Year":year, "Agency":agency, "URL":link} for id, title, year, size, price, agency, link in zip(ids, titles, years, sizes, prices, agencies, links)}
        """
    def writeData(self, filename):
        """
        Writes data scraped from website to json file.
        """
        json_string = json.dumps(self.data, ensure_ascii=False, indent=4)
        f = open(filename, "w", encoding='utf-8')
        f.write(json_string)
        f.close()