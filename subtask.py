import requests
from requests.auth import HTTPBasicAuth
import json

baseUrl="https://jira.consensuscorpdev.com/rest/api/2/issue"
headers = {'content-type' : 'application/json'}
jiraUser=''
jiraPassword=''

def bodyBuilder(subtask):
	projectObj={"key":subtask[0]}
	parentObj={"key":subtask[1]}
	issueType={"id":"5"}
	customfield_10722={"self": "https://jira.consensuscorpdev.com/rest/api/2/customFieldOption/13804","value": "Macondo "}
	assigneeObj={"name":subtask[4]}
	fieldsObj={"project":projectObj,"parent":parentObj,"summary":subtask[2],"description":subtask[3],"issuetype":issueType,"customfield_10721":subtask[5],"customfield_10722":customfield_10722,"assignee":assigneeObj}
	return fieldsObj

def createSubTask(subtask):
	dataObj={'fields':bodyBuilder(subtask)}
	print(dataObj)
	r=requests.post(baseUrl,auth=HTTPBasicAuth(jiraUser, jiraPassword), data = json.dumps(dataObj),headers=headers)
	print(r.text)

def defineSubtasksForESBMigration(parent,assignee):
	defaultSubTasks=[]
	carrierCall=["CC",parent,"Carrier Call","Change Rest call to carrier call using the new invoker for pam proxy",assignee,"new invoker using pam proxy implementation is working as is expected"]
	defaultSubTasks.append(carrierCall)
	raml=["CC",parent,"Replace RAML classes","Replace RAML classes in the mapping, add the messageHeader mapping",assignee,"messageHeader mapping and request body mapping using the new generated classes"]
	defaultSubTasks.append(raml)
	errorHandling=["CC",parent,"Implement common error handling","Change the old error handling with the new common error handling, add the enumeration classes for the current API.",assignee,"use the new analyze response subworkflow"]
	defaultSubTasks.append(errorHandling)
	responseUsages=["CC",parent,"Response usages","Review response usages. Fix the response usages to support the new classes",assignee,"All the response usages uses the new classes"]
	defaultSubTasks.append(responseUsages)
	pamDb=["CC",parent,"Check pamDBs","check that the pamDBs are being stored as before; otherwise, check the usages and fix it",assignee,"pamDBs are being used as is expected."]
	defaultSubTasks.append(pamDb)
	codeReview=["CC",parent,"Code review","Code review from other team member is required",assignee,"another team member approved the changes"]
	defaultSubTasks.append(codeReview)
	bddExecution=["CC",parent,"BDD Execution","BDD Execution for ESB and PAM Proxy sides succesfully",assignee,"Must execute a BDD passing thru the ESB and PAM Proxy paths succesfully, compare request XMLs"]
	defaultSubTasks.append(bddExecution)
	return defaultSubTasks


defaultSubTasks=defineSubtasksForESBMigration("CC-6689","hdelgado")


for i in defaultSubTasks:
	createSubTask(i)




