import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

website_html = response.text
# parse html with BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
# list comprehension is used as getText() cannot be aplyed to list
movie_titles = [movie.getText() for movie in all_movies]
# reversing list where -1 is last number, -1 is very last number 100 as 0 would show 99 only,
# -1 is step which is backwards
# for n in range(len(movie_titles) -1, -1, -1):
#     print(movie_titles[n])

# could also use:
# movies = sorted(movie_titles, reverse=True)

# this is list in reversed order
movies = movie_titles[::-1]

# writing the list into text file
with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
