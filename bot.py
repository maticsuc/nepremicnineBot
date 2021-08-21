import requests, time
from bs4 import BeautifulSoup
from src.tools import WebScraper

URL = "https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/?s=16"

bot = WebScraper(URL)

bot.scrapePage()

bot.writeDataToJSON("data/appartments.json")