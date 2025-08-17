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
    h2_tags = soup.find_all("h2")  # collects both titles and scales

    for idx in range(0, len(h2_tags), 2):
        try:
            title = h2_tags[idx].get_text(strip=True)
            scale = h2_tags[idx+1].get_text(strip=True)
            
            # Find the next text node containing "Image:"
            next_node = h2_tags[idx+1].find_next_sibling(text=True)
            img_url = None
            if next_node and next_node.strip().startswith("Image:"):
                # Extract URL portion from the string
                img_part = next_node.strip()[len("Image:"):].strip()
                img_url = img_part  # this could also be a filename or relative URL

            posts.append({
                "title": title,
                "scale": scale,
                "image": img_url
            })
        except IndexError:
            break

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

    while page < 110:
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}&p={page}"

        print(f"Fetching page {page}: {url}")
        soup = fetch_site(url)
        posts = get_posts(soup)

        if not posts:
            print("No more posts, stopping.")
            break

        for post in posts:
            print(post["title"], post["scale"], post["image"])
            #Download_Post(post["image"], folder, post["title"])

        page += 1


if __name__ == "__main__":
    main()