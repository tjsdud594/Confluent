#!/bin/bash

if [ -d ~/confluent ]
then 
    rm -rf ~/confluent && mkdir ~/confluent && cd ~/confluent
else
    mkdir ~/confluent && cd ~/confluent
fi

curl -O https://packages.confluent.io/archive/7.6/confluent-7.6.0.tar.gz
tar xzf confluent-7.6.0.tar.gz

CONFLUENT_PATH=~/confluent/confluent-7.6.0
CHECK_DIRS="/bin /etc /lib /libexec /share /src"

for dir in $CHECK_DIRS
do
    if [ -d ${CONFLUENT_PATH}${dir} ]
    then 
        echo "${CONFLUENT_PATH}${dir} --------------- Exist"
    else
        echo "${CONFLUENT_PATH}${dir} ---------------ERROR!!!!! Not Exist"
    fi
done

export CONFLUENT_HOME=~/confluent/confluent-7.6.0
export PATH=$PATH:$CONFLUENT_HOME/bin
echo "export CONFLUENT_HOME=~/confluent/confluent-7.6.0" >> ~/.bashrc
echo "export PATH=$PATH:$CONFLUENT_HOME/bin" >> ~/.bashrc
source ~/.bashrc

confluent local services start