# openMRS-API-Test

Hi! Guys for my final year project i have been experimenting with [openMRS](https://openmrs.org/). I have lerarned many things, but there is a famous quote that 

“_The more you know, the more you know you don't know._” ~ __Aristotle__

## What is inside this repository

There are two main files here in this repository: 

*latestEncounter.py 
*patientMedicalRecord.py.

### latestEncounter.py

It takes openMRS ID of patient as an input and returns you a dictionary which contains following information regarding latest encounter/vistit of patient to facility:

* Services
* Symptioms
* Diagnosis (ICD - 10 - WHO Coded) 

### patientMedicalRecord.py

It takes also takes openMRS ID of patient as an and returns you a dictionary which contains following information regarding all the past vistits of patient to facility:

* Patient UUID
* Patient OpenMRS ID
* Visit ID
* Start Date
* End Date
* Services
* Symptioms
* Diagnosis (ICD - 10 - WHO Coded)

### Things needed to run this code 
* python with required packages
* openMRS instance
* enter your own username and password in `HTTPBasicAuth(username,password)`

**GOOD LUCK, Happy Coding**


