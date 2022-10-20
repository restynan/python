#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
'''
#print(soup.title)
#print(soup.title.string)
# if there are may a tags , it return the first a tag
print(soup.a)

print(soup.find_all(name="a"))

#To get  h1 with an id
print(soup.find(name="h1", id="name"))

#To get  h3 with a class
print(soup.find_all(name="h3", class_="heading"))

#To get what is inside the anchor tags
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))
'''
#using css selectors
#select_one gives us the first matching item
company_url = soup.select_one(selector="p a")
print(company_url)
print(soup.select_one(selector="#name"))

# list of headings with class heading
print(soup.select(".heading"))

