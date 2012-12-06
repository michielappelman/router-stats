#!/bin/bash
#
# This script outputs the pretty XML with interface statistics from the router.
#
# Requirements:
#   - cURL
#   - node.js
#   - tidy (could be removed)


code=`curl http://192.168.0.1 2>/dev/null | grep -e ^auth_url | cut -d'=' -f4 | cut -d'"' -f1`
salt=`curl http://192.168.0.1 2>/dev/null | grep "salt =" | cut -d'"' -f2`
url=`node get-url.js $salt $code`

curl $url >/dev/null 2>&1
curl http://192.168.0.1/interface_stats.xml 2>/dev/null | tidy -xml 2>/dev/null
