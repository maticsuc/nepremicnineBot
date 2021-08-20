import requests, time
from bs4 import BeautifulSoup
from tools import WebScraper


URL = "https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/?s=16"

bot = WebScraper(URL)

bot.scrapePage()

"""

for i in r:
    print(i.text)



r.find("span")

print(r.text)

while True:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    st_stanovanj = soup.find("div", class_="oglasi_cnt").find("strong").text
    
    f = open("n.txt", "r")
    st_stanovanj_prej = f.read()

    if int(st_stanovanj) > int(st_stanovanj_prej):
        st_novih_stanovanj = int(st_stanovanj) - int(st_stanovanj_prej)
        if st_novih_stanovanj == 1:
            print(f"Dodano novo stanovanje! Trenutnih stanovanj je {st_stanovanj}.")
        elif st_novih_stanovanj == 2:
            print(f"Dodani 2 novi stanovanji! Trenutnih stanovanj je {st_stanovanj}.")
        else:
            print(f"Dodanih {st_novih_stanovanj} novih stanovanj! Trenutnih stanovanj je {st_stanovanj}.")

        f = open("n.txt", "w")
        f.write(st_stanovanj)
        f.close()

    if int(st_stanovanj) < int(st_stanovanj_prej):
        st_odstranjenih_stanovanj = int(st_stanovanj_prej) - int(st_stanovanj)
        if st_odstranjenih_stanovanj == 1:
            print(f"Stanovanje je bilo odstranjeno! Trenutnih stanovanj je {st_stanovanj}.")
        elif st_odstranjenih_stanovanj == 2:
            print(f"2 stanovanji sta bili odstranjeni! Trenutnih stanovanj je {st_stanovanj}.")
        else:
            print(f"{st_odstranjenih_stanovanj} stanovanj je bilo odstranjenih! Trenutnih stanovanj je {st_stanovanj}.")

        f = open("n.txt", "w")
        f.write(st_stanovanj)
        f.close()

    time.sleep(60)
"""