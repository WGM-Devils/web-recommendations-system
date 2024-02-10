import base_info as bi
import requests
import pandas as pd

uribase = bi.baseuri()

def get_all_posts():
    """
    Retrieves all posts from the API and prints the response.
    """
    uri = uribase + "/posts/all"
    responds_answer = requests.get(uri, headers={"Authorization": "KlingtGut"})
    print(responds_answer.json())
    print()
    print("----------------------------------------")
    print()

def get_user_likes():
    """
    Retrieves the likes of a specific user from the API and prints the response.
    """
    uri = uribase + "/users/get/id=65846334e4aa365544dd06af/type=json"
    responds_answer = requests.get(uri, headers={"Authorization": "KlingtGut"})
    print(responds_answer)
    print()
    print(responds_answer.json())
    print()
    responds_answer = responds_answer.json()
    responds_answer = responds_answer["response"]
    responds_answer = responds_answer["contents"]
    responds_answer = responds_answer["likes"]
    responds_answer = responds_answer["collection"]
    post_ids = []
    for i in responds_answer:
        post_id = i["id"]
        post_ids.append(post_id)
    print(responds_answer)
    print()
    print(post_ids)

# Uncomment the functions below to use them

get_all_posts()
# get_user_likes()
