import requests
from bs4 import BeautifulSoup

# News webscrapper
def main():
url = "https://www.example.com/news"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
articles = soup.find_all("div", class_="article")

# Extracting data from the website
for article in articles:
    title = article.find("h2").text
    link = article.find("a")["href"]
    summary = article.find("p").text
    print(title, link, summary)

# main function
if __name__ == "__main__":
    main()