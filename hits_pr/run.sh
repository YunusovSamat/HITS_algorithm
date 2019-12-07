#!/bin/bash

# Функция для запуска MapReduce.
runMapReduce () {
    # Переменная для указания номера входной папки
    counter=$1
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -D mapreduce.job.name="HITS algorithm Job via Streaming" \
    -files `pwd`/map.py,`pwd`/reduce.py \
    -input "hits/inOut$counter/" \
    -output "hits/inOut$((counter+1))"/ \
    -mapper `pwd`/map.py \
    -reducer `pwd`/reduce.py
}

# Если количество итераций не передано.
if [[ -z $1 ]]; then
    # Вывод ошибки и выход.
    echo "Error: argument not specified"
    exit 1
# Если количество итераций меньше одного.
elif (( $1 < 1 )); then
    # Вывод ошибки и выход.
    echo "Error: argument < 1"
    exit 1
fi

# Скрипт для отправки первых входных данных в hdfs.
./copyInput.sh
ITER_COUNT=$1
for ((i=1; i <= ${ITER_COUNT}; i++)); do
    runMapReduce ${i}
done