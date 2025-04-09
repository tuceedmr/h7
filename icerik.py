import requests
from bs4 import BeautifulSoup

def content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title_tag = soup.find("h1")
    title = title_tag.get_text().strip() if title_tag else ""

    time_tag = soup.find("time")
    tarih = time_tag.get_text().strip() if time_tag else ""

    paragraphs = soup.find_all("p")
    icerik = "\n".join([p.get_text().strip() for p in paragraphs])

    data = 'Tarih: {}\nBaşlık: {}\nİçerik:\n{}\n'.format(tarih, title, icerik)

    with open("haber_kayitlari.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")

content("https://www.milligazete.com.tr/haber/24244937/serdar-haydanli-kimdir")
