#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json, requests

key = '5994e27e6844480fb23bdc59d62e6c39'
token = 'e57c3b332557d35a09dafb47b0fd4a2ff3fd97e767b968c7a9e959fb312008ae'

r = requests.get("https://api.trello.com/1/cards/546214aca5632192c4615aa5/actions?key=5994e27e6844480fb23bdc59d62e6c39&token=04959d1f85d25556b66088b25b14fe8d4d8c8aa464078170821ecf10e741f044")

# charset=utf8
r.headers['content-type']
r.encoding = 'ISO-8859-1'
cards = json.loads(r.content)

print cards[0]["memberCreator"]["fullName"]

# print comments[0]

# f = file('testxxx.json','w')
# f.write("teste arquivo")
# f.close()
