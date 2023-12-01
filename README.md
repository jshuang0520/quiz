# preface

This project serves as a tool specifically crafted to facilitate a streamlined review of GRE vocabularies. While various tools, such as Magoosh flashcards, exist in the market, this particular product stands apart due to its unique design that caters to personalized requirements.

This product boasts several advantages. Firstly, it offers flexibility by enabling users to review vocabularies in various modes. Specifically, individuals can opt for sequential or random vocabulary reviews within a specified range. Moreover, users can determine the number of words to review under different circumstances. Secondly, the product automatically collects data during question answering for comprehensive analysis. This includes recording the time taken for each answer, correct rates for each vocabulary, and the usage of hints, allowing users to focus on reviewing their least familiar words in the future. Thirdly, the product provides users with a second chance for a quick review when they provide an incorrect answer. For instance, I have found it highly efficient to memorize an unfamiliar word within the next five seconds after providing an incorrect answer. This feature addresses a gap in current products, as similar solutions are not readily available. Lastly, the product is open-sourced, reflecting my belief in making education accessible to everyone. By making this project public, I encourage my friends preparing for the GRE test to utilize and benefit from it.


note. The initial version of this project was made in only two days (and it was for GRE vocab only), so the quality of code can be enhanced in the future. 

---

# user guide

- download docker desktop
 
- [docker build](#docker-build)

- [docker run](#docker-run) (with volume, to one of your directory) to get inside the docker container

  - [take a quiz](#take-a-quiz)

![quiz_ing](images/quiz_ing.png)

    - to determine how many question you are going to answer

    - to determine the mode: (1) random (2) in a specific range

![quiz_mode](images/quiz_mode.png)

    - if you are wrong, review it for 5 sec(s) in default

![review_5_sec](images/review_5_sec.png)

  - [check errors](#check-errors) (optional)

![check_error](images/check_error.png)    


Hopefully this tool may help you. Enjoy it!

--

# sample command to run (on your local computer):


## docker build

- first, download docker and build your docker image

```
bash scripts/build_docker_img.sh
```


## docker run

- command template:

```
docker run \
-v [DIR_ON_YOUR_LOCAL_MACHINE]:[DIR_IN_DOCKER] \
-it [YOUR_DOCKER_IMAGE_NAME] \
/bin/bash
```

e.g.
```
docker run \
-v /Users/johnson.huang/py_ds/tutor_python_project/bookmarks/GRE_prepare/GRE_vocab/MasonGRE_2000/quiz:/quiz \
-it quizlet/version \
/bin/bash
```


## take a quiz

- after you enter the docker container, take a quiz

```
bash scripts/run.sh
```

```
# pattern of docker volumn:     [real world dir] : [inside docker dir]

docker run -v REAL_WORLD_DIR:INSIDE_DOCKERDIR -it YOUR_DOCKER_IMAGE_NAME /bin/bash

#docker run -v /Users/johnson.huang/py_ds/tutor_python_project/bookmarks/GRE_prepare/GRE_vocab/MasonGRE_2000/quiz:/quiz -it quizlet/version /bin/bash


#docker run \
#-v /Users/johnson.huang/py_ds/tutor_python_project/bookmarks/GRE_prepare/GRE_vocab/MasonGRE_2000/quiz:/dokodemo_door \
#quizlet/version:latest \
#bash scripts/run.sh
```


## check errors

- check recent error records

```
bash scripts/check_recent_error.sh
```
