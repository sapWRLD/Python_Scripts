import os 
import praw
import urllib.request
from Reddit import reddit1

script_dir = os.path.dirname(os.path.abspath(__file__))
folders_exists = False
reddit = reddit1 # Enter your own praw.reddit creds
subreddits = [reddit.subreddit('RealGirls'),
              reddit.subreddit('NSFW_GIF'),
              reddit.subreddit('nsfw'),
              reddit.subreddit('pcmasterrace'),
              reddit.subreddit('cats')]

def make_Folder():
    global folders_exists
    global script_dir
    

    nsfw_path = os.path.join(script_dir, 'nsfw_Images')
    sfw_path = os.path.join(script_dir, 'sfw_Images')
    
    if not os.path.isdir(nsfw_path):
        os.mkdir(nsfw_path)
        print(f"Created folder: {nsfw_path}")
    
    if not os.path.isdir(sfw_path):
        os.mkdir(sfw_path)
        print(f"Created folder: {sfw_path}")
    
    if os.path.isdir(nsfw_path) and os.path.isdir(sfw_path):
         folders_exists = True
    return

def fetch_Images():
    global subreddits
    global script_dir
    image_Count = 0
    for subreddit in subreddits:
        print(f"Fetching from r/{subreddit.display_name}")
        for post in subreddit.new(limit=15):
            if not post.is_video and not hasattr(post, "gallery_data"):
                if post.url.endswith((".jpeg", "jpg", ".png", ".gif")) or (hasattr(post, "post_hint") and post.post_hint == "image"):
                    print("image found!", post.title, post.url)
                    try:
                        if post.over_18:
                            file_path = os.path.join(script_dir, 'nsfw_Images', f"{post.id}.jpeg")
                            urllib.request.urlretrieve(post.url, file_path)
                            image_Count =+ 1
                        else:
                            file_path = os.path.join(script_dir, 'sfw_Images', f"{post.id}.jpeg")
                            urllib.request.urlretrieve(post.url, file_path)
                            image_Count =+ 1
                        print(f"Downloaded {file_path}")
                        
                    except Exception as e:
                        print(f"Failed to download {post.url}: {e}")
    print(f"Puller image ({image_Count} Pulled).")


def main():
    make_Folder()
    if folders_exists == True:
        fetch_Images()
if __name__ == "__main__":
    main()