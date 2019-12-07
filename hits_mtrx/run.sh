#!/bin/bash


runMapReduce () {
    counter=$1
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -D mapreduce.job.name="HITS algorithm Job via Streaming" \
    -files `pwd`/map.py,`pwd`/reduce.py \
    -input "hits/inOut$counter/" \
    -output "hits/inOut$((counter+1))"/ \
    -mapper `pwd`/map.py \
    -reducer `pwd`/reduce.py
}


if [[ -z $1 ]]; then
    echo "Error: argument not specified"
    exit 1
elif (( $1 < 1 )); then
    echo "Error: argument < 1"
    exit 1
fi

copyInput.sh
ITER_COUNT=$1
for ((i=1; i <= ${ITER_COUNT}; i++)); do
    runMapReduce ${i}
done