# Recommendations System for KlingtGut

## Contents:
* [Get hashtags from a seen post](#get-hashtags-from-a-seen-post)
* [Score post based on hashtags for user](#score-post-based-on-hashtags-for-user)

## Setup:

### Requirements:

* python 3.11
* pip

#### Libraries:

* requests
* pandas
* numpy
* python-dateutil

> [!NOTE]
> you only need to install pip than you can run the following command to install the libraries
> ```bash
> python ./hashtags_for_user/base_info.py
> ```
> this will install all the required libraries

#### Files:

* base_info.py
* hashtags_from_post.py
* post_score.py

> [!WARNING]
> you need to have all the files in the same folder named hashtags_for_user


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

```csv
hashtags-{userid}-.csv
```

example:

```csv
hashtags-65846334e4aa365544dd06af-.csv
```

#### Filelayout:

syntax:

|`none`|viewed|liked|comments|posted|score|
|:---:|:---:|:---:|:---:|:---:|:---:|
|test|0|0|0|0|0|
|{hashtag}|{a}|{b}|{c}|{d}|{$`a + 10 * b + 5 * c + 10 * d`$}|

layout:

```csv
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

```csv
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
python /location/to/file/post_score.py {userid} {postid}
```

example:

```bash
python hashtags_for_user/post_score.py 65846334e4aa365544dd06af 65b111bdd0ba272101646dad
```

### Output:

#### Filename:

syntax:

```csv
post-scores-{userid}-.csv
```

example:

```csv
post-scores-65846334e4aa365544dd06af-.csv
```

#### Filelayout:

syntax:

|`none`|viewed|score|
|:---:|:---:|:---:|
|0|False|0.0|
|{postid}|{boolean}|{$`postscore / nhashtags + likes * 10`$}|

layout:

```csv
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

```csv
,viewed,score
0,False,0.0
65b111bdd0ba272101646dad,False,70.0
```

</details>