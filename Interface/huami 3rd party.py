import re
import urllib2
import json
from urllib2 import URLError


return_url='''
https://account-staging-us.mi-ae.com/oauth2/REGISTERed#access_token=TQVBQDpyQktGXip6SltGeiouXAQABAAAAAJKlXsS4b3Av3DScoB0BJ6ILQS5ubXOwf2QpYRtlWA_H3zXKoZR3clJs76CxhMHRtpVO_byksSCKIS4w64uyR8qVxykiNNwJSkbncyGRBZyVIGBrlAO5EQKdJVz8bCXFSpxv8sFH9tIEdeeKtOzI4wLwCh6ImNuJ14o7FWGSF8xbVWR18O8gyG1AZjbJNwpkWRpM7eOnY9JlyodptkKduvw&expires_in=7776000&state=BLACK_BOX
'''
#return_url='https://account-staging-us.mi-ae.com/oauth2/REGISTERed#access_token=TQVBQDpyQktGXip6SltGeiouXAQABAAAAAAhJ-652yHj-f9aproy1SWAbt0vzLXr5ChU-YhPNJf49e0j93wHq4mpMwE249W_8AfH463BLrV8q2sTtqDLqnZcguI9CiaFKoQnIYYDte3_qRua2nRgZplCrw3JHvr2h47Wj4Qqnx0JeUrFuhKGGmR8T8aY26nsCG_s_XEvq-1Doi3VM4uAnhL94s8nXCYxQco7KiqJspXrUb_PrtmYlUK8&expires_in=7776000&state=BLACK_BOX'

key=r'access_token=(.*?)&expire'
pattern=re.compile(key)
match=re.findall(pattern,return_url)
token='Bearer '+match[0]
print "TOKEN:"
print token

#reqst=urllib2.Request('https://api-open-staging-us.mi-ae.com/users/-/profile')
#reqst=urllib2.Request('https://api-open-staging-us.mi-ae.com/users/-/activities?startDate=2016-03-26&endDate=2017-05-10&interval=daily')
#reqst=urllib2.Request('https://api-open-staging-us.mi-ae.com/users/-/sleep?startDate=2017-05-02&endDate=2017-05-03&interval=hourly')
reqst=urllib2.Request('https://api-open-staging-us.mi-ae.com/users/-/heartrates?startDate=2017-05-10&endDate=2017-05-10')
#reqst=urllib2.Request('https://api-open-staging-us.mi-ae.com/users/-/motionInMinute?startDate=2017-05-10&endDate=2017-05-11')

reqst.add_header('Authorization',token)


try:
    resp=urllib2.urlopen(reqst)
    #print resp.headers
    resp_data = resp.read()
    json_format = json.dumps(json.loads(resp_data), sort_keys=True, indent=4)
    print(json_format)

except URLError, e:
    print "ERROR CODE: "+str(e.code)
    print e.read()
    print






#====================================================
#base_url='https://api-open-staging-us.mi-ae.com'

# api_user='users/-/profile'
# api_activity='/users/-/activities?startDate=2016-08-05&endDate=2017-08-06&interval=daily'
# api_sleep='/users/-/sleep?startDate=2016-08-05&endDate=2017-08-06&interval=daily'
# api_hr='/users/-/sleep?startDate=2016-08-05&endDate=2017-08-06&interval=daily'
# api_mim='/users/-/motionInMinute?startDate=2016-08-05&endDate=2017-08-06'
#
#
# api_user_url=base_url+api_user
# api_activity_url=base_url+api_activity
# api_sleep_url=base_url+api_sleep
# api_hr_url=base_url+api_hr
# api_mim_url=base_url+api_mim
#======================================================





