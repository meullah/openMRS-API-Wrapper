import requests
from requests.auth import HTTPBasicAuth
import json


patient_openMRS_id = '1003A5' 
get_uuid = 'http://localhost:8080/openmrs-standalone/ws/rest/v1/patient?q={}&&v=custom:uuid'.format(patient_openMRS_id)
res = requests.get(get_uuid,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()

patient_uuid = res['results'][0]['uuid']

# print(patient_uuid)

visits_url = "http://localhost:8080/openmrs-standalone/ws/rest/v1/visit?patient={}&&v=full".format(patient_uuid)
res = requests.get(visits_url,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()
# data = res['results'][0]['encounters']

visit = [patient_uuid,patient_openMRS_id]

for data in res['results']:
    temp = {}
    diagnosis_links  =[]
    providers_list=[]
    
    temp['visit_id'] = data['uuid']
    temp['start_date'] = data['startDatetime']
    temp['end_date'] = data['stopDatetime']
    temp['services'] = []
    temp['symptoms'] = []
    temp['diagnosis'] = []
    for encounter in data['encounters']:
        for provider in encounter['encounterProviders']:
            if provider['display'].split(':')[0] not in providers_list:
                providers_list.append(provider['display'].split(':')[0]) 

        if encounter['form']['display']=='Lab Exam':
            temp['services']+= encounter['obs'][0]['display'][24:].split(',')
        elif encounter['form']['display']=='Visit Note':
            if encounter['obs'] != []:
                temp['symptoms'] += encounter['obs'][0]['display'][24:].split(',')
            for j in encounter['diagnoses']:
                diagnosis_links.append(j['links'][0]['uri'])


        for url in diagnosis_links:
            res = requests.get(url,auth=HTTPBasicAuth('meullah', 'Ehsan@123')).json()
            # print(url)
            if 'coded' in res['diagnosis']:
                for i in res['diagnosis']['coded']['mappings']:
                    if i['display'][:3] == 'ICD':
                        temp['diagnosis'].append(i['display'][12:])

    temp['providers'] = providers_list

    visit.append(temp)

print(visit)

