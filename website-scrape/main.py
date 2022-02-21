from bs4 import BeautifulSoup
import requests

link = "https://news.ycombinator.com/"

html_contents = requests.get(link).text
# print(html_contents.text)

soup = BeautifulSoup(html_contents, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))              # Get the actual Link

span = soup.find_all(name="span", class_="score")
article_upvotes = [int(score.getText().split()[0]) for score in span]


# print(article_texts)
# print(article_links)
print(len(article_upvotes))

max_index = article_upvotes.index(max(article_upvotes))
# print(max_index)
# print(article_upvotes)
print(article_texts[max_index])



