#[ -z "$1" ] && echo "specify enviroment" && exit
#ENV="${1}"
#docker build -f Dockerfile -t living_area/"${ENV}"_model:latest . --no-cache

docker build -f Dockerfile -t quizlet/version:latest . --no-cache
