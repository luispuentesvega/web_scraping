from requests import get
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/search/title?release_date=2018&sort=num_votes,desc&page=1'

response = get(url)
#print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))
#First movie
first_movie = movie_containers[0]
#print(first_movie)
print(first_movie.h3.a.text)