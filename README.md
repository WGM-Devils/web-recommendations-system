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

layout:
```
,viewed,liked,comments,posted,score
test,0,0,0,0,0
```