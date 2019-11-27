#!/bin/bash

hdfs dfs -rm -r hits

hdfs dfs -mkdir -p hits/input

hdfs dfs -put matrix*.txt hits/input/