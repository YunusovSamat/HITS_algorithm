#!/bin/bash

hdfs dfs -rm -r hits
hdfs dfs -mkdir -p hits/inOut1

cd ~/PycharmProjects/TaskPackage/HITS_algorithm/
hdfs dfs -put matrix*.txt hits/inOut1/