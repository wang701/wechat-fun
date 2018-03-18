#!/usr/bin/env python
# -*- coding: utf-8 -*-

import search_google.api
import os

from wxpy import *

# Set developer key and CSE ID
with open(os.path.expanduser('.secrets/dev_key'), 'r') as f:
		dev_key = f.read().replace('\n', '')

with open(os.path.expanduser('.secrets/cse_id'), 'r') as f:
		cse_id = f.read().replace('\n', '')

bot = Bot()
only_one = ensure_one(bot.friends().search(u'毛毛虫宝宝'))

@bot.register(msg_types=TEXT)
def print_others(msg):
    print msg.text
    print dev_key, cse_id

		# Define buildargs for cse api
    buildargs = {
        'serviceName': 'customsearch',
        'version': 'v1',
        'developerKey': dev_key
    }

    # Define cseargs for search
    cseargs = {
        'q': msg.text,
        'cx': cse_id,
        'num': 3
    }
    # Create a results object
    results = search_google.api.results(buildargs, cseargs)
    print results
    only_one.send(results.links)

bot.join()
