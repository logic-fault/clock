clock
=====

Quick hack to clock in and out to add to your crontab or maybe run from shell

* set username and password in clockin.py and clockout.py
* set domain to companyName.com
* add to crontab

```
	55 8 * * 1-5 user /home/user/clockin.py
	05 17 * * 1-5 user /home/user/clockout.py
```
