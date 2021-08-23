from src.tools import WebScraper
from datetime import datetime
import time, json

URL = "https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/"

json_file = "data/number_of_appartments.json"

bot = WebScraper(URL)

nAppartments_temp = bot.nAppartments
current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

json_string = json.dumps({current_time:nAppartments_temp}, ensure_ascii=False, indent=4)
f = open(json_file, "w", encoding='utf-8')
f.write(json_string)
f.close()

while True:
    if bot.getNappartments() != nAppartments_temp:
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        f = open(json_file, "r", encoding='utf-8')
        json_string = f.read()
        data = json.loads(json_string)
        data[current_time] = bot.nAppartments
        json_string = json.dumps(data, ensure_ascii=False, indent=4)
        f = open(json_file, "a", encoding='utf-8')
        f.write(json_string)
        f.close()
        nAppartments_temp = bot.nAppartments

    time.sleep(60)