#!/bin/bash

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="HITS Job via Streaming" \
-files map.py,reduce.py \
-input hits/inOut1 \
-output hits/inOut2 \
-mapper map.py \
-reducer reduce.py

hdfs dfs -cat hits/inOut2/part-00000