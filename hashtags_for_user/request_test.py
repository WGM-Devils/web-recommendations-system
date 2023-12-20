import requests
import pandas as pd

uri = "https://hallo.klingt-gut.repl.co/api/posts/all"

posts = requests.get(uri, headers={"Authorization": "KlingtGut"}).json()

print(posts)

n = 0

posts_with_ids = []

for post in posts["posts"]:
    print(post)
    n += 1
    
    post_id = post["id"]
    print(post_id)
    
    full_post = {post_id: post}
    
    posts_with_ids.append(full_post)

print(posts_with_ids)