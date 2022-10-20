#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://news.ycombinator.com/
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

#print(soup.title)
#print(soup.find_all(name="span", class_="score"))

articles = soup.select(".titleline a")
article_texts = []
article_links = []

for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get('href'))


article_upvotes = [int(score.getText().split()[0]) for score in soup.select(".score")]

print(article_texts)
print(article_links)
print(article_upvotes)

#find index of the highest score
max_score = max(article_upvotes)
max_index = article_upvotes.index(max_score)
print(max_index)

# print the most popular article and link
print(article_texts[max_index])
print(article_links[max_index])

#you cannot commercialise copyrighted content
#you can't scape data behind  Authentication
#https://news.ycombinator.com/robots.txt
#https://www.linkedin.com/robots.txt