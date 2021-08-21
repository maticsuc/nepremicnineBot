import requests, time
from bs4 import BeautifulSoup
from tools import WebScraper

URL = "https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/?s=16"

bot = WebScraper(URL)

bot.scrapePage()

#bot.writeData("data.json")