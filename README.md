# Recommendations System for KlingtGut

## Contents:
* [Get hashtags from a seen post](#get-hashtags-from-a-seen-post)
* [Score post based on hashtags for user](#score-post-based-on-hashtags-for-user)


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
|{hashtag}|{a}|{b}|{c}|{d}|{$`a + 10 * b + 5 * c + 10 * d`$}|


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



<details>
<summary>layout:</summary>

```
,viewed,liked,comments,posted,score
test,0,0,0,0,0
#musik,5,4,1,1,60
#python,5,4,1,1,60
```

</details>

## Score post based on hashtags for user
### command:

syntax:

```bash
python /location/to/file/post_score.py 65846334e4aa365544dd06af 65b111bdd0ba272101646dad
```

example:

```bash
python hashtags_for_user/post_score.py 65846334e4aa365544dd06af 65b111bdd0ba272101646dad
```

### Output:
#### Filename:

syntax:
```
post-scores-{userid}-.csv
```

example:
```
post-scores-65846334e4aa365544dd06af-.csv
```

#### Filelayout:

syntax:

|`none`|viewed|score|
|:---:|:---:|:---:|
|0|False|0.0|
|{postid}|{boolean}|{$`postscore / nhashtags + likes * 10`$}|


layout:
```
,viewed,score
0,False,0.0
```


example:

|`none`|viewed|score|
|:---:|:---:|:---:|
|0|False|0.0|
|65b111bdd0ba272101646dad|False|70.0|



<details>
<summary>layout:</summary>

```
,viewed,score
0,False,0.0
65b111bdd0ba272101646dad,False,70.0
```

</details>