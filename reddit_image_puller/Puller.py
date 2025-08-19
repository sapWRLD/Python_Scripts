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
            if not hasattr(post, "gallery_data"):
                if post.is_video or post.url.endswith((".jpeg", ".jpg", ".png", ".gif", ".gifv", ".mp4")) \
                    or (hasattr(post, "post_hint") and post.post_hint in ["image", "hosted:video"]):

                    try:
                        if post.is_video:
                            video_data = None
                            if post.media and "reddit_video" in post.media:
                                video_data = post.media["reddit_video"]
                            elif post.secure_media and "reddit_video" in post.secure_media:
                                video_data = post.secure_media["reddit_video"]

                            if video_data:
                                duration = video_data.get("duration", 0)
                                if duration > 30:
                                    print(f"Skipping {post.id} (too long: {duration}s)")
                                    continue

                                url = video_data["fallback_url"]
                                ext = ".mp4"
                            else:
                                print(f"Skipping {post.id}, could not find video data")
                                continue

                        else:
                            # Normal images/gifs
                            url = post.url
                            ext = os.path.splitext(url)[1] if "." in url else ".jpg"

                        folder = "nsfw_Images" if post.over_18 else "sfw_Images"
                        file_path = os.path.join(script_dir, folder, f"{post.id}{ext}")
                        urllib.request.urlretrieve(url, file_path)
                        image_Count += 1
                        print(f"Downloaded {file_path}")

                    except Exception as e:
                        print(f"Failed to download {post.url}: {e}")

    print(f"Pulled {image_Count} files.")



def main():
    make_Folder()
    if folders_exists == True:
        fetch_Images()
if __name__ == "__main__":
    main()