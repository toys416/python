# importing the requests library
import requests
import ssl

# api-endpoint
# URL = "https://test.jenkins.drillops.slb.com/job/ttt/build"

user = 'jwang309'
token = '1177ec372e9ebf75638a95922619bcec8b'
URL = "https://cd.drillopstown.slb.com/job/SyncEnv.XX.Core.BatchTrigger/buildWithParameters"

# defining a params dict for the parameters to be sent to the API
# Environments = ['Qat','Nam','Eur','Ksa','Om']
Environments = ['Nam2']
CMRID = '2042069'
targetScopes = 'Core'
version = 'Stable'
serviceWhiteList = 'Slb.Prism.Core.Service.Rig-2'
SyncEnvJob = 'SyncEnv.XX.Core'

form_data  = {
    'SyncEnvJob':SyncEnvJob,
    'CDPkgVersion':'Stable',
    'targetScopes':targetScopes,
    'serviceWhiteList':serviceWhiteList,
    'version':version,
    'ChunkSize':'20',
    'allowDowngrade':'true',
    'CMRID':CMRID    
    }

# sending get request and saving the response as response object
# r = requests.get(url = URL, params = PARAMS)
# r = requests.post(url = URL,auth=('jwang309', '116c68e7f3dc2221e4ff57c9283957c04a'),verify=False)   //ttt

for env in Environments:
    URL = URL.replace('XX',env)
    SyncEnvJob = SyncEnvJob.replace('XX',env)

    print(URL)
    print(SyncEnvJob)
    r = requests.post(url = URL,auth=(user,token),data = form_data, verify=False)   



