#!/usr/bin/python
#  quick hack: auto clock-in tool

import urllib2
import urllib 
import cookielib

username = '' # enter your username for internal
password = '' # enter your password for internal
domain   = '' # enter your company domain


refer = 'https://internal.' + domain + '/account/login'
argUrl = 'https://internal.' + domain + '/account/login'
clock = 'https://internal.' + domain + '/account/clock/in?id='
logout = 'https://internal.' + domain + '/account/logout'

#setup cookies
cookies = cookielib.LWPCookieJar()
handlers = [
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.HTTPCookieProcessor(cookies)
    ]
opener = urllib2.build_opener(*handlers)

#setup POST data for login
params = urllib.urlencode({'name': username}) + '&' + urllib.urlencode({'password': password})

# open login page
req = urllib2.Request(url=refer)
f = opener.open(req)

#login
req = urllib2.Request(url=argUrl, data=params)
req.add_header('Referer', refer);
f = opener.open(req)

#find the clock id
id_search_str = '/account/clock/in?id='
data = f.read()
before_id = data.find(id_search_str)
after_id  = data.find('\">', before_id)

#cut out the id
id_start = before_id + len(id_search_str)
id       = data[id_start:(after_id - 1)]

#clock in
req=urllib2.Request(url=(clock + id))
opener.open(req)

#log out
req = urllib2.Request(url=logout)
opener.open(req)
