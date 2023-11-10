import pandas
import os.path


user = "113231132311323113231132311323" #User ID
userFile = "hashtags " + user + ".csv"
if os.path.isfile(userFile):
    pass
else:
    f = open(userFile, "w")
    f.write("hashtag,viewed,time,liked,disliked,comments,posted,score")
    f.write("\ntest,1,10,5,3,2,1,77")
df = pandas.read_csv(userFile, index_col="hashtag", sep=",")

hashtags1 = [] #definiert die Liste hashtag1
check = "#" #da durch wir jeder hastag erkannt
splitPostSubSentinses = []
post = "Dies ist ein #Test Post für #Python. So das ist, der zweite, Satz ich nutze #VS-Code um zu #programmieren." #Post von dem man den Hastag haben will
print(post) #druckt Post in Terminal nur zum debuggen

postdot = post.rfind(".") #Findet vom hintersten Punkt im Post die Position
post = post[:postdot] #Löscht den hintersten Punkt im Post
print(post) #druckt Post in Terminal nur zum debuggen

splitPostSentinses = post.split(". ") #trent den Post an jebem Punkt mit Lehrzeichen danach und schreibt in Liste ohne Punkte
print(splitPostSentinses) #druckt List von forheriger Line in Terminal nur zum debuggen

for satz in splitPostSentinses:
    if ', ' in satz:
        splitPostSubSentinses.extend(satz.split(", "))
    else:
        splitPostSubSentinses.append(satz)

print(splitPostSubSentinses)

for subSatz in splitPostSubSentinses:                                                       #(
    hashtags = [idx for idx in subSatz.split() if idx[0].lower() == check.lower()]          # sucht alle hashtags aus den Sätzen und fügt sie alle als einzelne Items in die Liste hashtags1
    hashtags1.extend(hashtags)                                                              #)

print(hashtags1) #druckt List hashtags1 in Terminal nur zum debuggen

print(df)
