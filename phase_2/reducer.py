#!/bin/python3

import sys
import json
import re


def tokenize(text):
    words = re.findall(r'\w+', text)
    return set(words)

def jaccard(A, B):
    return len(A.intersection(B)) / len(A.union(B))

for line in sys.stdin:
    pairing = json.loads(line.strip())
    news_companies = list(pairing.items())
    if len(news_companies) >= 2:
        
        company_A_tokens = tokenize(news_companies[0][1])  
        company_B_tokens = tokenize(news_companies[1][1])  
        
        pairing['similarity'] = jaccard(company_A_tokens, company_B_tokens)
    
    print(news_companies[0][0],"VS",news_companies[1][0]," similarity: ", pairing['similarity'])
