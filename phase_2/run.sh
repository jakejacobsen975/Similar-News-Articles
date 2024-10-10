#!/bin/bash
rm -r phase_2/jaccard
hadoop jar /home/jake/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
    -mapper phase_2/mapper.py \
    -reducer phase_2/reducer.py \
    -input phase_1/articles/part-00000 \
    -output phase_2/jaccard
