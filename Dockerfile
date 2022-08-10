FROM python:3.8-slim
MAINTAINER johnson.huang
ENV INSTALL_PATH /quiz
ENV PYTHONPATH=$PYTHONPATH:$INSTALL_PATH

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y apt-transport-https && \
    apt-get install -y vim && \
    echo Y | apt-get install default-jre && \
    pip install --upgrade pip && \
    pip install wheel  && \
    pip install -r requirements.txt --no-cache-dir
    
# # For AWS Systems Manager Parameter Store
# RUN apt-get update && \
#     apt-get install -y apt-transport-https && \
#     apt-get install -y build-essential ca-certificates wget gcc g++ && \
#     rm -rf /var/lib/apt/lists/* && \
#     wget https://github.com/segmentio/chamber/releases/download/v2.3.3/chamber-v2.3.3-linux-amd64 -O /usr/local/bin/chamber && \
#     chmod +x /usr/local/bin/chamber
    
WORKDIR ${INSTALL_PATH}

COPY . .
# COPY lib/mysql-connector-java-8.0.28.jar mysql-connector-java-8.0.28.jar

RUN chmod +x ${INSTALL_PATH}/scripts/*.sh


#CMD ['python', 'parse_quizlet_mason2000.py']

