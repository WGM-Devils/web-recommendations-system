import 
import requests
import pandas as pd
'''
uri = "https://b0fc8dd9-5d36-49bb-a59b-82f1a484f310-00-1dnjn7p68t02k.global.replit.dev/posts/all"


posts = requests.get(uri, headers={"Authorization": "KlingtGut"}).json()

print(posts)
print()
n = 0

posts_with_ids = []

posts = posts["response"]
print(posts)
print()

posts = posts["contents"]

for post in posts["posts"]:
    print(post)
    print()
    n += 1
'''

'''uri = "https://b0fc8dd9-5d36-49bb-a59b-82f1a484f310-00-1dnjn7p68t02k.global.replit.dev/users/all/type=json"

responds_answer = requests.get(uri, headers={"Authorization": "KlingtGut"})

print(responds_answer.json())'''



uri = "https://klingt-gut.cyclic.app/api/posts/get/id=659ea34d10f8e1ccfa27ed8f/type=json"

responds_answer = requests.get(uri, headers={"Authorization": "KlingtGut"})

print(responds_answer)
print()
print(responds_answer.json())
print()

responds_answer = responds_answer.json()

responds_answer = responds_answer["response"]
responds_answer = responds_answer["contents"]
responds_answer_content = responds_answer["content"]
responds_answer_title = responds_answer["title"]

print(responds_answer_content)
print()
print(responds_answer_title)

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