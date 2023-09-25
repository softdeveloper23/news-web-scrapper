import requests
from bs4 import BeautifulSoup

# News webscrapper
def main():
url = "https://www.example.com/news"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

# main function
if __name__ == "__main__":
    main()