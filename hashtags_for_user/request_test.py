import requests
import pandas as pd

#uri = "https://b0fc8dd9-5d36-49bb-a59b-82f1a484f310-00-1dnjn7p68t02k.global.replit.dev/api/posts/all"


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

'''

uri2 = "https://b0fc8dd9-5d36-49bb-a59b-82f1a484f310-00-1dnjn7p68t02k.global.replit.dev/users/get/id=65846334e4aa365544dd06af/type=json"

response_uri2 = requests.get(uri2, headers={"Authorization": "KlingtGut"})

print(response_uri2)

if response_uri2.status_code == 200:
    print("200")
    print(response_uri2.json())
else:
    print("404")

'''