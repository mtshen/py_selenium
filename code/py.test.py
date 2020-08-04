import re
matchObj = re.match('^.+/static/auth-manage/#/login\\??.+$', 'http://localhost:8080/static/auth-manage/#/login1?systemCode=AVALON&r=http%3A%2F%2F172.16.43.170%2Fstatic%2Fark%2F%23%2Fworkstation')
print(matchObj)
