"""
This script calculates the score for a given post based on the hashtags used in the post, the number of likes the post has received, and the time elapsed since the post was created.

The script takes two command-line arguments: User ID and Post ID. It retrieves information about the user and post from an API and performs the following steps:

1. Checks if the User ID and Post ID are valid.
2. Reads the user's hashtag data from a CSV file.
3. Reads the post score data from a CSV file.
4. Extracts hashtags from the post content.
5. Calculates the score for each hashtag based on the user's hashtag data.
6. Calculates the overall post score by combining the hashtag scores, number of likes, and time elapsed since the post was created.
7. Updates the post score data in the CSV file.

Note: This script assumes the existence of the following files:
- "hashtags-{user_id}.csv": Contains the user's hashtag data.
- "post-scores-{user_id}.csv": Contains the post score data.

Usage: python post_score.py <user_id> <post_id>
"""

import pandas as pd
import os.path
import sys
import requests
import base_info as bi
import datetime
import dateutil.parser
import random


n = len(sys.argv)
try:
    if n != 3:
        print("Please enter a valid User ID and Post ID")
        exit()
    
    uribase = bi.baseuri()

    if len(sys.argv[1]) == 24:
        user = str(sys.argv[1])
        user_check_uri = uribase + f"/users/get/id={user}/type=json"
        response_user_check = requests.get(url=user_check_uri, headers={"Authorization": "KlingtGut"})
        print(response_user_check.json())
        if response_user_check.status_code == 200:
            pass
        else:
            print("User ID is not valid")
            exit()
    else:
        print("User ID is not valid")
        exit()

    if len(sys.argv[2]) == 24:
        post_id = str(sys.argv[2])
        post_id_check_uri = uribase + f"/posts/get/id={post_id}/type=json"
        response_post_check = requests.get(url=post_id_check_uri, headers={"Authorization": "KlingtGut"})
        if response_post_check.status_code == 200:
            response_post_check = response_post_check.json()
            response_post_check = response_post_check["response"]
            response_post_check = response_post_check["contents"]
            post = response_post_check["content"]
            time_post = response_post_check["createdAt"]
            time_post = dateutil.parser.parse(time_post)
        else:
            print("Post ID is not valid")
            exit()
    else:
        print("Post ID is not valid")
        exit()

    
    # get likes of post
    post_likes = response_post_check["likes"]
    post_likes = post_likes["count"]
    print()
    print(post_likes)
    print()
    
    userFile =  "hashtags-" + user + "-.csv"
    postScoreFile = "post-scores-" + user + "-.csv"
    if os.path.isfile(userFile):
        pass
    else:
        f = open(userFile, "w")
        f.write("hashtag,viewed,liked,comments,posted,score")
        f.write("\ntest,1,1,1,1,1")
        f.close

    if os.path.isfile(postScoreFile):
        pass
    else:
        f = open(postScoreFile, "w")
        f.write("post,viewed,score")
        f.write("\n0,False,0")
        f.close()

    df = pd.read_csv(userFile, index_col=0, sep=",")
    df_post = pd.read_csv(postScoreFile, index_col=0, sep=",")

    hashtags1 = [] #definiert die Liste hashtag1
    hashtags2 = []
    check = "#" #da durch wir jeder hashtag erkannt
    splitPostSubSentences = []
    post_score = 0
    c = 0
    #post = "Dies ist ein #Test Post für #Python. So das ist, der zweite, Satz ich nutze #VS-Code um zu #programmieren." #Post von dem man den Hashtag haben will TODO: must be changed when I add the apis to the code 
    print(post) #druckt Post in Terminal nur zum debuggen

    postDot = post.rfind(".") #Findet vom hintersten Punkt im Post die Position
    post = post[:postDot] #Löscht den hintersten Punkt im Post
    print(post) #druckt Post in Terminal nur zum debuggen

    splitPostSentences = post.split(". ") #trennt den Post an jedem Punkt mit Leerzeichen danach und schreibt in Liste ohne Punkte
    print(splitPostSentences) #druckt List von vorheriger Line in Terminal nur zum debuggen

    for satz in splitPostSentences:
        if ', ' in satz:
            splitPostSubSentences.extend(satz.split(", "))
        else:
            splitPostSubSentences.append(satz)

    print(splitPostSubSentences)

    for subSatz in splitPostSubSentences:                                                       # TODO: for ö, ü, ä implement recognition and then replace with oe, ue, ae
        hashtags = [idx for idx in subSatz.split() if idx[0].lower() == check.lower()]          # sucht alle hashtags aus den Sätzen und fügt sie alle als einzelne Items in die Liste hashtags1
        hashtags1.extend(hashtags)                                                              #)

    print(hashtags1) #druckt List hashtags1 in Terminal nur zum debuggen

    print(df)

    for hashtag in hashtags1:
        print(hashtag.lower())
        hashtags2.append(hashtag.lower())

    print(df)


    for hashtag in hashtags2:
        if hashtag in df.index.to_list():
            print(f'der score von {hashtag} ist: {df.at[hashtag,"score"]}')
            post_score = post_score + df.at[hashtag,"score"]
        else:
            print(f'{hashtag} ist nicht in der liste also ist der Standartwert: 100')
            post_score = post_score + 100
            
        c = c + 1
    
    print(f'der Post Score ist: {post_score}')
    if c == 0:
        print("there are no hashtags in this post")
        exit()

    time_now = datetime.datetime.now(datetime.timezone.utc)
    # get time between post and now in hours and every thing under 1 hour is a float number
    time_between_post_and_now = time_now - time_post
    
    post_score = post_score / c + (post_likes * 10) / (time_between_post_and_now.total_seconds() / 3600) + random.randint(0, 50)

    
    print(f'der Post Score durch die Anzahl der Hashtags ist: {post_score}')

    if post_id in df_post.index.to_list():
        print(post_id, 'is in csv')
        df_post.at[post_id,"score"] = post_score
    else:
        print(post_id, 'is not in csv')
        new_row = {post_id:[False,post_score]}
        df_new_row = pd.DataFrame.from_dict(data=new_row,
                                            orient='index',
                                            columns=[
                                                "viewed",
                                                "score"
                                            ])
        print(new_row)
        print(df_new_row)
        df_post = pd.concat([df_post, df_new_row])

    print(df_post)

    df_post.to_csv(postScoreFile)
except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")
    exit()
except:
    print("An error has occurred.")
    exit()