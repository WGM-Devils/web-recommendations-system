import pandas as pd
import os.path
from pandas import *
import sys

n = len(sys.argv)

if n != 3:
    print("Please enter a valid User ID and Post ID")
    exit()

if len(sys.argv[1]) == 30:
    user = str(sys.argv[1]) #User ID must be changed when I add the apis to the code 
else:
    print("User ID is not valid")
    exit()

if len(sys.argv[2]) == 30:
    post_id = str(sys.argv[2]) #Post ID must be changed when I add the apis to the code
else:
    print("Post ID is not valid")
    exit()

userFile =  "hashtags-" + user + "-.csv"
postScoreFile = "post-scores-" + user + "-.csv"
if os.path.isfile(userFile):
    pass
else:
    f = open(userFile, "w")
    f.write("hashtag,viewed,time,liked,disliked,comments,posted,score")
    f.write("\ntest,1,1,1,1,1,1,1")
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
post = "Dies ist ein #Test Post für #Python. So das ist, der zweite, Satz ich nutze #VS-Code um zu #programmieren." #Post von dem man den Hashtag haben will TODO: must be changed when I add the apis to the code 
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
print(f'der Post Score durch die Anzahl der Hashtags ist: {post_score / c}')

if post_id in df_post.index.to_list():
    print(post_id, 'is in csv')
    df_post.at[post_id,"score"] = post_score / c
else:
    print(post_id, 'is not in csv')
    new_row = {post_id:[False,post_score / c]}
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
