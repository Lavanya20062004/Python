import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "http://quotes.toscrape.com"

# Send a GET request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote blocks
quotes = soup.find_all("div", class_="quote")

# Extract and print quotes and authors
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"{text} — {author}")