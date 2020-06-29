import requests
from requests.auth import HTTPBasicAuth

patient_openMRS_id = '1003A5' 
get_uuid = 'http://localhost:8080/openmrs-standalone/ws/rest/v1/patient?q={}&&v=custom:uuid'.format(patient_openMRS_id)
res = requests.get(get_uuid,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()

patient_uuid = res['results'][0]['uuid']

print(patient_uuid)
visits_url = "http://localhost:8080/openmrs-standalone/ws/rest/v1/visit?patient={}&&v=full".format(patient_uuid)
res = requests.get(visits_url,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()
data = res['results'][0]['encounters']

dignosis_links = []
dignosis_list = []
symptoms = []
services = []
for i in data:
    if i['form']['display']=='Lab Exam':
        services = i['obs'][0]['display'][24:].split(',')
        print(services)
    elif i['form']['display']=='Visit Note':
        if i['obs'] != []:
            symptoms = i['obs'][0]['display'][24:].split(',')
        for j in i['diagnoses']:
            dignosis_links.append(j['links'][0]['uri'])



for url in dignosis_links:
    res = requests.get(url,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()
    # print(res['diagnosis']['coded']['mappings'])
    for i in res['diagnosis']['coded']['mappings']:
        if i['display'][:3] == 'ICD':
            dignosis_list.append(i['display'][12:])

print(dignosis_list)

# print([0]['diagnoses'] == [])
