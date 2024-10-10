#!/bin/bash
rm -r phase_1/articles
hadoop jar /home/jake/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
    -mapper phase_1/mapper.py \
    -reducer phase_1/reducer.py \
    -input phase_1/Inputfiles/cnbc.json \
    -input phase_1/Inputfiles/ksl_articles_9-24.json \
    -input phase_1/Inputfiles/ksl_articles_9-26.json \
    -input phase_1/Inputfiles/ksl_articles_9-27.json \
    -input phase_1/Inputfiles/the_verge.json \
    -output phase_1/articles





