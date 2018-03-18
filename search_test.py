#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
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
    'q': '习近平',
    'cx': cse_id,
    'num': 10
}

# Create a results object
results = search_google.api.results(buildargs, cseargs)

# Download the search results to a directory
print results.links
