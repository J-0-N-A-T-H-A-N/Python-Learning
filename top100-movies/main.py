import requests
from bs4 import BeautifulSoup
import os

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

html_content = requests.get(URL).text

soup = BeautifulSoup(html_content, "html.parser")

movie_list = soup.find_all(name="h3", class_="title")
reverse_list = [movie.getText() for movie in movie_list]    # List comprehension

with open("movie_list.txt", mode="w") as movie_file:
    for movie in reversed(reverse_list):
        movie_file.write(f"{movie}\n")
