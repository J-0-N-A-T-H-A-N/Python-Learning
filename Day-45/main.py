from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.li)

# all_anchors = soup.find_all(name="a")
# for tag in all_anchors:
#     print(tag.getText())
#     print(tag.get("href"))

# USING CSS SELECTORS
# company_url = soup.select_one(selector="p a")
# print(company_url)
# print(company_url.get("href"))
# name = soup.select_one(selector="#name")
# print(name)
# print(name.getText())

# heading = soup.find_all(name="h1", id="name")
# print(heading)
#
# heading_3 = soup.find(name="h3", class_="heading")      # NOTE class_ rather than class
# print(heading_3.getText())
# print(heading_3.name)
# print(heading_3.get("class"))

ordered_list = soup.find(name="ul")
print(ordered_list)
