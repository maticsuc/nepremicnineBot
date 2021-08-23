from src.tools import WebScraper

URL = "https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/?s=3"

bot = WebScraper(URL)

bot.scrapeAllPages()

bot.writeDataToJSON("data/appartments.json")