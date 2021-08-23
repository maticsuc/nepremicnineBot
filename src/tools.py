import requests, json, urllib.parse
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.base_url = self.url.rsplit('/', 1)[0]
        self.data = dict()

        self.getNextPage()
        self.getNappartments()

    def getNappartments(self):
        """
        Returns (and sets) number of all found appartments.
        """
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")

        try:
            self.nAppartments = int(soup.find("div", {"class":"oglasi_cnt"}).find("strong").text)
        except:
            self.nAppartments = None

        return self.nAppartments

    def getNextPage(self):
        """
        Returns (and sets) the next page of current page. None if current page doesn't have the next page.
        """
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            self.nextPage = urllib.parse.urljoin(self.url, soup.find("a", {"class":"next"})['href'])
        except:
            self.nextPage = None

        return self.nextPage

    def scrapePage(self):
        """
        Scrapes webpage for appartments and saves them to dictionary.
        """

        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        list = soup.find("div", {"class":"seznam"}).find_all("div", {"class":"oglas_container"})

        for i in list:
            position = id = title = size = price = year = level = agency = link = type = None
            try:
                position = i.find("meta", {"itemprop":"position"})['content']
                id = int(i.find("a")['title'])
                title = i.find("a").find("span", {"class":"title"}).text
                size = float(i.find("span", {"class":"velikost"}).text.replace(" m2", "").replace(",","."))
                price = float(i.find("meta", {"itemprop":"price"})['content'])
                year = i.find("span", {"class":"atribut leto"}).find("strong").text
                level = i.find("span", {"class":"atribut"}).text.split(" ")[1].replace(",","") if len(i.find("span", {"class":"atribut"})['class']) == 1 else ""
                agency = i.find("div", {"class":"prodajalec_o"})['title']
                link = urllib.parse.urljoin(self.base_url, i.find("a")['href'])
                type = i.find("span", {"class":"tipi"}).text
                
            except:
                pass

            if id not in self.data and id is not None:
                self.data[id] = {"title":title, "type":type, "size":size, "price":price, "year":year, "level":level, "agency":agency, "url":link}

    def scrapeAllPages(self):
        """
        Scrapes all appartments on all next pages.
        """
        nPages = 0
        while True:
            if self.nextPage is not None:
                self.scrapePage()
                nPages += 1
                self.url = self.nextPage
                self.getNextPage()
            else:
                self.scrapePage()
                nPages += 1
                break

        return f"Scraped {nPages} pages, Total appartments: {len(self.data)}"

    def writeDataToJSON(self, filename):
        """
        Writes data scraped from website to JSON file.
        """
        json_string = json.dumps(self.data, ensure_ascii=False, indent=4)
        f = open(filename, "w", encoding='utf-8')
        f.write(json_string)
        f.close()
    
    def readDataFromJSON(self, filename):
        """
        Reads data from JSON file.
        """
        pass