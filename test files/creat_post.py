import base_info as bi
import requests

uribase = bi.baseuri()
uri = uribase + "/api/posts/create"

def create_post():
    """
    Creates a post using the API and prints the response.
    """
    data = {
    "title": input("Enter title: "), 
    "content": input("Enter content: "),
    "embed": {
        "type": "image",
        "link": input("Enter link: ")
    }, 
    "userId": "65846334e4aa365544dd06af"
}
    responds_answer = requests.post(uri, headers={"Authorization": "KlingtGut"}, json=data)
    print(responds_answer)

create_post()