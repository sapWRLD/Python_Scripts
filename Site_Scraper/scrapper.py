import requests
from bs4 import BeautifulSoup
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_site(url):
    site = requests.get(url, headers=HEADERS)
    return BeautifulSoup(site.text, 'html.parser')


def make_folder():
    global SCRIPT_DIR
    Posts_path = os.path.join(SCRIPT_DIR, 'Posts')
    if not os.path.isdir(Posts_path):
        os.mkdir(Posts_path)
        print(f"Created folder: {Posts_path}.")
        return
    return Posts_path

def get_posts(soup):
    posts = []

    containers = soup.find_all("div", class_="kolom midden")
    for box in containers:
        #print(box.prettify())  # show what you actually found (debug)

        title_tag = box.find("h2", class_="titel")
        scale_tag = box.find("h2", class_="scale")
        img_tag = box.find("img")

        title = title_tag.get_text(strip=True) if title_tag else None
        scale = scale_tag.get_text(strip=True) if scale_tag else None
        img_url = img_tag["src"] if img_tag else None

        posts.append({
            "title": title,
            "scale": scale,
            "image": img_url
        })
    return posts


def Check_For_Images():
    return

def Download_Post():
    return


def main():
    url = "https://www.lambodiecast.com/list.php?m=Lamborghini"
    soup = fetch_site(url)
    posts = get_posts(soup)
    make_folder()
    
    for post in posts:
        print(post["title"], post["image"])

    return
if __name__ == "__main__":
    main()