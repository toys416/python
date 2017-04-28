import re
import urllib2
import json


url='http://amazfit-staging-admin.private.mi-ae.cn/ECGHealthData?userId=1000000203&startDay=2017-01-01&endDay=2017-01-07&limit=5'

reqst=urllib2.Request(url)
reqst.add_header('Authorization','Basic cm9vdDphZG1pbg==')

resp=urllib2.urlopen(reqst)
resp_data=resp.read()

json_format = json.dumps(json.loads(resp_data),sort_keys=True,indent=4)
print(json_format)


key=r'\"heartRate.*?,'
pattern=re.compile(key)
match=re.findall(pattern,resp_data)


print match








