#!/bin/python3

import sys
import json
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

for line in sys.stdin:
    if line.strip():
        if line == ':::kaggle_news_articles\t\n':
            continue
        print(line)
