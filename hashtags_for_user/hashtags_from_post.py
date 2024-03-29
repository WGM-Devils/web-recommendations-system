"""
This script extracts hashtags from a given post and updates a CSV file with the hashtag statistics.

The script takes two command-line arguments: User ID and Post ID. It verifies the validity of the User ID and Post ID by making API requests. If the IDs are valid, it retrieves the post content and extracts hashtags from it. It then updates a CSV file with the hashtag statistics, including the number of times each hashtag has been viewed, liked, commented on, and posted.

The script uses the following external libraries:
- pandas: for reading and writing CSV files
- os.path: for checking if a file exists
- random: for generating random numbers
- requests: for making API requests

Usage: python hashtags_from_post.py <User ID> <Post ID>
"""

import pandas as pd
import os.path
import random
import sys
import requests
import base_info as bi


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
    
    postScoreFile = "post-scores-" + user + "-.csv"
    userFile =  "hashtags-" + user + "-.csv"
    
    if os.path.isfile(userFile):
        pass
    else:
        f = open(userFile, "w")
        f.write("hashtag,viewed,liked,comments,posted,score")
        f.write("\ntest,0,0,0,0,0")
        f.close()

    if os.path.isfile(postScoreFile):
        pass
    else:
        f = open(postScoreFile, "w")
        f.write("post,viewed,score")
        f.write("\n0,False,0")
        f.close()
    
    df = pd.read_csv(userFile, index_col=0, sep=",")
    df_post = pd.read_csv(postScoreFile, index_col=0, sep=",")
    

    # check if post id is valid and get post content
    if len(sys.argv[2]) == 24:
        post_id = str(sys.argv[2])
        post_id_check_uri = uribase + f"/posts/get/id={post_id}/type=json"
        response_post_check = requests.get(url=post_id_check_uri, headers={"Authorization": "KlingtGut"})
        if response_post_check.status_code == 200:
            response_post_check = response_post_check.json()
            response_post_check = response_post_check["response"]
            response_post_check = response_post_check["contents"]
            post = response_post_check["content"]
            if post_id in df_post.index.to_list():
                if df_post.at[post_id,"viewed"] == True:
                    print("Post has already been viewed")
                    exit()
                else:
                    df_post.at[post_id,"viewed"] = True
        else:
            print("Post ID is not valid")
            exit()
    else:
        print("Post ID is not valid")
        exit()

    hashtags1 = [] #definiert die Liste hashtag1
    hashtags2 = []
    check = "#" #da durch wir jeder hashtag erkannt
    splitPostSubSentences = []
    print(post) #druckt Post in Terminal nur zum debuggen

    uri_like = uribase + f"/users/get/id={user}/type=json"
    like_responds = requests.get(uri_like, headers={"Authorization": "KlingtGut"})
    if like_responds.status_code == 200:
        like_responds = like_responds.json()

        like_responds = like_responds["response"]
        like_responds = like_responds["contents"]
        like_responds = like_responds["likes"]
        like_responds = like_responds["collection"]
        like_ids = []
        for i in like_responds:
            like_id = i["id"]
            like_ids.append(like_id)
        for i in like_ids:
            if i == post_id:
                like = True
                break
            else:
                like = False
    else:
        like = False
    comment = False

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
    
    # turn all hashtags to lowercase
    hashtags1 = hashtags2
    hashtags2 = []
    for hashtag in hashtags1:
        print(hashtag.lower())
        hashtags2.append(hashtag.lower())

    for hashtag in hashtags2:
        if hashtag in df.index.to_list():
            print(hashtag, " is in csv")
            df.at[hashtag,"viewed"] = df.at[hashtag,"viewed"] + 1
            print(df.at[hashtag,"viewed"])
            
            if like == True:
                df.at[hashtag,"liked"] = df.at[hashtag,"liked"] + 1

            if random.randrange(0,4) == 3:
                df.at[hashtag,"comments"] = df.at[hashtag,"comments"] + 1
            elif random.randrange(0,3) == 2:
                df.at[hashtag,"posted"] = df.at[hashtag,"posted"] + 1
                
            df.at[hashtag,"score"] = df.at[hashtag,"viewed"] + 10 * df.at[hashtag,"liked"] + 5 * df.at[hashtag,"comments"] + 10 * df.at[hashtag,"posted"]
        else:
            print(hashtag, " is not in csv")
            
            if like == True:
                like_n = 1
            else:
                like_n = 0

            new_row = {hashtag:[1,like_n,0,0,1+10*like_n+5*0+10*0]} #TODO: must be changed when I add the apis to the code 
            df_new_row = pd.DataFrame.from_dict(data=new_row,
                                                orient='index',
                                                columns=[
                                                    "viewed",
                                                    "liked",
                                                    "comments",
                                                    "posted",
                                                    "score"
                                                ])
            print(new_row)
            print(df_new_row)
            df = pd.concat([df, df_new_row])

    print(df)
    '''print(hashtag in df.index.to_list())
    if hashtag in df.index.to_list():
        print('yes')
    else:
        print('no')'''

    df.reset_index
    print(df)

    df.to_csv(userFile)
except KeyboardInterrupt:
    print("KeyboardInterrupt has been caught.")
    exit()
except:
    print("An error has occured.")
    exit()