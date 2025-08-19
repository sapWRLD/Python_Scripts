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

SITE_ROOT = "https://www.lambodiecast.com/"

def get_posts(soup):
    posts = []
    h2_tags = soup.find_all("h2", class_="titel")  # only grab titles

    for h2 in h2_tags:
        title = h2.get_text(strip=True)

        # Find the next <h2 class="scale">
        scale_tag = h2.find_next_sibling("h2", class_="scale")
        scale = scale_tag.get_text(strip=True) if scale_tag else None

        # Find the next <img class="hoofding">
        img_tag = h2.find_next("img", class_="hoofding")
        img_url = SITE_ROOT + img_tag["src"].lstrip("/") if img_tag else None

        posts.append({
            "title": title,
            "scale": scale,
            "image": img_url
        })

    return posts



def Check_For_Images():
    return

"""def Download_Post(url, folder, title):
    if not url:
        return
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        ext = url.split('.')[-1]
        filename = f"{title}.{ext}".replace('/', '_')
        path = os.path.join(folder, filename)
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}")"""

def main():
    base_url = "https://www.lambodiecast.com/list.php?m=Lamborghini"
    folder = make_folder()
    page = 1
    total_posts = 0

    while page <= 110: #site has 110 page's
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}&p={page}"   #Sites uses P= instead of page=

        print(f"Fetching page {page}: {url}")
        soup = fetch_site(url)
        posts = get_posts(soup)

        if not posts:
            print("No more posts, stopping.")
            break

        for post in posts:
            print(post["title"], post["scale"], post["image"])
            total_posts += 1
            #Download_Post(post["image"], folder, post["title"])

        page += 1

    print(f"\n✅ Scraped a total of {total_posts} posts.")


if __name__ == "__main__":
    main()