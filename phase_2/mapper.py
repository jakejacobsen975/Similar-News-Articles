#!/bin/python3

import sys
import itertools
import json
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


ksl = ""
cnbc = ""
the_verge = ""

for line in sys.stdin:
    line = line.strip()
    if line:
        url, content = line.split(':::')
        if 'ksl.com' in url:
            ksl += content
        elif 'cnbc.com' in url:
            cnbc += content
        elif 'theverge.com' in url:
            the_verge += content


all_articles = [ ksl, cnbc,the_verge]
# format is <url>:::<content>
# combs = itertools.combinations(all_articles, 2)
# for comb in combs:
#     if comb[0] != line or not comb[1] or comb[0] == '\t':
#         continue
pairing = {'KSL': ksl, 'CNBC': cnbc}
print(json.dumps(pairing))

pairing = {'KSL': ksl, 'the verge': the_verge}
print(json.dumps(pairing))


pairing = {'the verge': the_verge, 'CNBC': cnbc}
print(json.dumps(pairing))
