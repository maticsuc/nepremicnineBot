import requests, time
from bs4 import BeautifulSoup
from src.tools import WebScraper

URL = "https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/"

bot = WebScraper(URL)

bot.scrapeAllPages()

#bot.scrapePage()

bot.writeDataToJSON("data/appartments.json")

print(len(bot.data))
