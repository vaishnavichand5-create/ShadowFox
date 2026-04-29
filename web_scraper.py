import requests
from bs4 import BeautifulSoup

url = "https://example.com"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("Page Title:", soup.title.string)

    print("\nLinks:")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            print(href)

    print("\nParagraphs:")
    for p in soup.find_all("p"):
        print(p.text)

else:
    print("Failed to fetch page")
