import requests
from bs4 import BeautifulSoup

url = "http://python123.io/ws/demo.html"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    # print(soup.prettify())
    # Upward Traversal
    for parent in soup.a.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)
except:
    print("FAILED")

print("Comment")
