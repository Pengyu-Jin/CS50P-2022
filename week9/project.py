from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import json
import instaloader
import random
from datetime import datetime
import os
import requests
import sqlite3



def load_cookies(loader):
    cookies_file = "instagram_cookies.json"
    if not os.path.exists(cookies_file):
        save_cookies_with_browser()
    with open("instagram_cookies.json", "r", encoding="utf-8") as file:
        cookies = json.load(file)
        for cookie in cookies:
            loader.context._session.cookies.set(cookie["name"], cookie["value"])


def save_cookies_with_browser():
    service = Service("./chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove the automation table header
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=service, options=options)

    # Preventing detection as automated operation, but with little effect.
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    })

    driver.get("https://www.instagram.com/")
    time.sleep(random.randint(2, 10))
    
    # wait for user to login
    print("Please log in to Instagram manually. Press Enter to continue after logging in...")
    input("Press Enter to continue after logging in...")
    
    # store the cookies of the user's Instagram account as a json file
    cookies = driver.get_cookies()
    with open("instagram_cookies.json", "w", encoding="utf-8") as file:
        json.dump(cookies, file, ensure_ascii=False, indent=4)
    driver.quit()

def init_db(goal_folder, db_name):
    db_path = os.path.join(goal_folder, db_name)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS instagram_data(
            id INTEGER PRIMARY KEY,
            title TEXT,
            hashtags TEXT,
            url TEXT,
            date TEXT,
            likes INTEGER,
            comments INTEGER,
            media_type TEXT,
            media_path TEXT
        )
    """)
    conn.commit()
    conn.close()
    return db_path



def download_post(loader, profile, max_posts=1, goal="", db_path=""):
    try:
        if max_posts == "":
            max_posts = 1
        else:
            max_posts = int(max_posts)
    
        post_count = 1
        print(f"Instagram account: {profile.username}")
        formatted_follower_count = f"{profile.followers:,}"
        print(f"Number of followers: {formatted_follower_count}")
        os.makedirs(goal, exist_ok=True)
        for post in profile.get_posts():
            if post_count <= max_posts:

                post_folder = os.path.join(goal, f"post_{post_count}")
                os.makedirs(post_folder, exist_ok=True)

                if post.is_video:
                    media_type = "video"
                    media_path = post_folder

                    vedio_url = post.video_url
                    filename = os.path.join(post_folder, f"{post.shortcode}.mp4")
                    download_video(filename, vedio_url)


                elif post.typename == "GraphSidecar":
                    # check if the post has multiple images
                    media_type = "graphsidecar"
                    media_path = post_folder

                    for index, node in enumerate(post.get_sidecar_nodes()):
                        filename = os.path.join(post_folder, f"{index+1}")
                        image_url = node.display_url
                        mtime = datetime.now()
                        loader.download_pic(filename, image_url, mtime)
                else:
                    # if the post has only one image
                    media_type = "singlegraph"
                    media_path = post_folder

                    filename = os.path.join(post_folder, "1")
                    image_url = post.url
                    mtime = datetime.now()
                    loader.download_pic(filename, image_url, mtime)

                post_url = f"https://www.instagram.com/p/{post.shortcode}/"
                title_withhashtag = post.caption.split("#")[0].strip()
                title = formatted_title(title_withhashtag)
                post_hashtags =" ".join(f"#{_}" for _ in post.caption_hashtags)
                formatted_likes = f"{post.likes:,}"
                formatted_comments = f"{post.comments:,}"

                # Save the data to the database
                data = (title_withhashtag, post_hashtags, post_url, post.date.strftime("%Y-%m-%d %H:%M:%S"), post.likes, post.comments, media_type, media_path)
                save_to_db(data, db_path)

                print(f"Post Title: \n{title}")
                print(f"Post Tags: {post_hashtags}")
                print(f"Post Link: {post_url}")
                print(f"Post Date: {post.date}")
                print(f"Number of Likes: {formatted_likes}")
                print(f"Number of Comments: {formatted_comments}")
                print(f"Media Type: {media_type}")
                print(f"Media Path: {media_path}")
                print("-------------------------")
                post_count += 1
            else:
                break
    except ValueError:
            print("Please enter an integer as the download quantity.")


def download_video(filename, url):
    response = requests.get(url)
    with open(filename, 'wb') as f:
            f.write(response.content)
    return True


def formatted_title(title):
    # Split the title by row
    lines = title.strip().split("\n")
    
    # Find the longest line and determine the length of the border
    max_length = max(len(line) for line in lines)
    border = "+" + "-" * (max_length + 2) + "+"
    
    # Construct dialog box
    formatted_title = border + "\n"
    for line in lines:
        formatted_title += f"| {line.ljust(max_length)} |\n"
    formatted_title += border
    
    # Returns the formatting result
    return formatted_title


def save_to_db(data,db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO instagram_data(title, hashtags, url, date, likes, comments, media_type, media_path)
        VALUES (?,?,?,?,?,?,?,?)
    """, data)
    conn.commit()
    conn.close()


def main():
    # using Instaloader load Cookies
    loader = instaloader.Instaloader(quiet=True)
    loader.context._session.cookies.clear()  # Clear original Cookies
    load_cookies(loader)

    goal = input("Please select the Instagramer name you want to download from: ")
    profile = instaloader.Profile.from_username(loader.context, goal) 
    max_posts = input("Please enter the number of posts to download (default is 1): ")

    # create the goal folder
    os.makedirs(goal, exist_ok=True)

    # initialize the database and get the path
    db_path = init_db(goal, f"{goal}.db")

    # pass the db_path to the download_post function
    download_post(loader, profile, max_posts, goal, db_path)
    

if __name__ == "__main__":
    main()