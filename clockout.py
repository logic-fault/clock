#!/usr/bin/python

#  quick hack: auto clock-out tool
import urllib2
import urllib 
import cookielib

username = '' # fill your internal username
password = '' # fill clock pw
domain   = '' # put your companyname.com

refer = 'https://internal.' + domain + '/account/login'
argUrl = 'https://internal.' + domain + '/account/login'
clock = 'https://internal.' + domain + '/account/clock/out?id='
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
id       = data[id_start:(after_id)]

#clock in
clockUrl = clock + id
req=urllib2.Request(url=clockUrl)
req.add_header('Referer', 'https://internal.' + domain + '/account/view?id=' + id)
opener.open(req)

print 'clockUrl = ' + clockUrl

#log out
req = urllib2.Request(url=logout)
opener.open(req)
