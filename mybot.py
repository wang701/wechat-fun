#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib
import random

import search_google.api
import googleapiclient.errors

from wxpy import *

# Set developer key and CSE ID
with open(os.path.expanduser('.secrets/dev_key'), 'r') as f:
		dev_key = f.read().replace('\n', '')

with open(os.path.expanduser('.secrets/cse_id'), 'r') as f:
		cse_id = f.read().replace('\n', '')

bot_err_msg = 'bot has some issues, please try again ...'
img_path = 'downloads/biaoqin.jpg'

bot = Bot(cache_path='wxpy.pkl')
print bot.groups()
my_group = bot.groups().search('Rex')
#my_friend = ensure_one(bot.friends().search(u'亚光'))

print my_group

@bot.register(chats=my_group, msg_types=TEXT, except_self=False)
def print_others(msg):
    print msg

    # check if the incoming msg contains the cmd string
    if msg.type == TEXT:
        if u'表情' in msg.text:
            print 'cmd found in text!'
            keyword_str = msg.text.strip(u'表情').encode('utf-8')
        else:
            print 'cmd not found in text!'
            return

    print keyword_str

		# Define buildargs for cse api
    buildargs = {
        'serviceName': 'customsearch',
        'version': 'v1',
        'developerKey': dev_key
    }
    # Define cseargs for search
    cseargs = {
        'q': '暴走表情' + keyword_str,
        'cx': cse_id,
        'num': 5,
        'searchType': 'image',
        'imgSize': 'medium',
        'fileType': 'jpg'
    }
    # Create a results object
    try:
        results = search_google.api.results(buildargs, cseargs)
    except googleapiclient.errors.HttpError as e:
        print e
        for friend in my_group:
            friend.send_msg(bot_err_msg)
        return
        #my_friend.send_msg(bot_err_msg)

    rand_ind = random.randint(0,4)

    print rand_ind

    print results.links
    print results.links[rand_ind]

    try:
        urllib.urlretrieve(results.links[rand_ind], img_path)
    except urllib.error as e:
        print e
        for friend in my_group:
            friend.send_msg(bot_err_msg)
        return
        #my_friend.send_msg(bot_err_msg)

    for friend in my_group:
        friend.send_image(img_path)
    #my_friend.send_image(img_path)

bot.join()
