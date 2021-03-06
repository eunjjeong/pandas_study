from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://news.khan.co.kr/kh_news/khan_art_view.html?artid=201705101228011"
html_mun = requests.get(url, headers=headers)
soup_mun = BeautifulSoup(html_mun.text, "lxml")

artists = soup_mun.find_all('p', {"class", "content_text"})
list_mun = [content.get_text() for content in artists]

df = pd.DataFrame(list_mun)
print(df.head())
df.to_csv("mun.csv")