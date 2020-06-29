import datetime,json
import requests
from requests.auth import HTTPBasicAuth


currentDateTime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
newVisits = []


req_url = 'http://localhost:8080/openmrs-standalone/ws/rest/v1/visit?includeInactive=true&fromStartDate={}&&v=full'.format('2020-06-28T21:59:41.145')

res = requests.get(req_url,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()

# print(res['results'][0].keys())

for visit in res['results']:
    visit_dict = {'visit_uuid' : visit['uuid'],'patient_uuid' : visit['patient']['uuid']} 
    visit_dict['start_datetime'] = visit['startDatetime']
    visit_dict['stop_datetime'] = visit['stopDatetime']
    visit_dict['services'] = []
    visit_dict['symptoms'] = []
    visit_dict['diagnosis'] = []
    diagnosis_links = []
    for encounter in visit['encounters']:
        if encounter['form']['display']=='Lab Exam':
            visit_dict['services'] += encounter['obs'][0]['display'][24:].split(',')
        elif encounter['form']['display']=='Visit Note':
            if encounter['obs'] != []:
                visit_dict['symptoms'] += encounter['obs'][0]['display'][24:].split(',')
            for j in encounter['diagnoses']:
                diagnosis_links.append(j['links'][0]['uri'])
    
    for url in diagnosis_links:
            res = requests.get(url,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()
            # print(url)
            if 'coded' in res['diagnosis']:
                for i in res['diagnosis']['coded']['mappings']:
                    if i['display'][:3] == 'ICD':
                        visit_dict['diagnosis'].append(i['display'][12:])

    
    newVisits.append(visit_dict)


print(newVisits)






