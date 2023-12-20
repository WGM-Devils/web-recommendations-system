import requests

uri = "https://hallo.klingt-gut.repl.co/api/posts/all"

print(requests.get(uri, headers={"Authorization": "KlingtGut"}).json())