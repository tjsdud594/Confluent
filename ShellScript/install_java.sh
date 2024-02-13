#!/bin/bash

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install openjdk-11-jdk -y

echo "java version : $(java --version)"

# 환경변수 추가
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))
echo "export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which java))))" >> ~/.bashrc
echo "export PATH=$PATH:$JAVA_HOME/bin" >> ~/.bashrc

source ~/.bashrc