#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import urllib

import search_google.api

with open(os.path.expanduser('.secrets/dev_key'), 'r') as f:
		dev_key = f.read().replace('\n', '')

with open(os.path.expanduser('.secrets/cse_id'), 'r') as f:
		cse_id = f.read().replace('\n', '')

# Define buildargs for cse api
buildargs = {
    'serviceName': 'customsearch',
    'version': 'v1',
    'developerKey': dev_key
}

# Define cseargs for search
cseargs = {
    'q': '暴走表情',
    'cx': cse_id,
    'num': 10,
    'searchType': 'image',
    'fileType': 'jpg'
}

# Create a results object
try:
    results = search_google.api.results(buildargs, cseargs)
except googleapiclient.errors.HttpError:
    print 'bot has some issue, please try again ...'

rand_ind = random.randint(1,10)

# Download the search results to a directory
print results.links
print results.links[rand_ind]

urllib.urlretrieve(results.links[rand_ind], 'downloads/biaoqin.jpg')
