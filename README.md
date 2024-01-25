# Recommendations System for KlingtGut
## Get hashtags from a seen post
### command:

syntax: 
```bash
python /location/to/file/hashtags_from_post.py {userid} {postid}
```

example: 
```bash
python hashtags_for_user/hashtags_from_post.py 65846334e4aa365544dd06af 65b111bdd0ba272101646dad
```

### Output:
#### Filename:
syntax:
```
hashtags-{userid}-.csv
```

example:
```
hashtags-65846334e4aa365544dd06af-.csv
```
#### Filelayout:
syntax:
|`none`|viewed|liked|comments|posted|score|
|:---:|:---:|:---:|:---:|:---:|:---:|
|test|0|0|0|0|0|
|{hashtag}|{a}|{b}|{c}|{d}|{$a + 10 * b + 5 * c + 10 * d$}

layout:
```
,viewed,liked,comments,posted,score
test,0,0,0,0,0
```

example:
|`none`|viewed|liked|comments|posted|score|
|:---:|:---:|:---:|:---:|:---:|:---:|
|test|0|0|0|0|0|
|#musik|5|4|1|1|60|
|#python|5|4|1|1|60|

layout:
```
,viewed,liked,comments,posted,score
test,0,0,0,0,0
#musik,5,4,1,1,60
#python,5,4,1,1,60
```
