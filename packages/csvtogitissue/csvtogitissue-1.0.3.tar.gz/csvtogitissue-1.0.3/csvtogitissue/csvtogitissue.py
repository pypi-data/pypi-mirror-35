import sys
import requests
import json
import os
import csv
import urllib
import urllib.request
import pandas as pd
import dateutil.parser as parser
from time import gmtime, strftime

#This function uses a Gform FileID to download a google form
#Returns 1 for success
#Returns 0 fo fail
def download_responses_gform(FILE_ID,FILE_NAME):

	try:
		toget = 'https://docs.google.com/spreadsheet/ccc?key='+FILE_ID+'&output=csv'
		urllib.request.urlretrieve(toget,FILE_NAME)
		return 1
	except Exception as e:
		print (e)
		return 0

#This function uses downloads the CSV via direct link
#Returns 1 for success
#Returns 0 fo fail
def download_responses_CSV(FILE_LINK,FILE_NAME):

	try:
		urllib.request.urlretrieve(FILE_LINK,FILE_NAME)
		return 1
	except Exception as e:
		print (e)
		return 0

#Iterates __create_github_issue for all the entries in the CSV
#This is called to run create issues
#Returns 1 for success
#Returns 0 fo fail
def create_issues(FILE_NAME,TOKEN,REPO_NAME,REPO_OWNER,TITLE,DESCRIPTION,LABELS,EMAIL,CREATED_DT):
	try:
		df = pd.read_csv(FILE_NAME, header=None)
		counter = 0
		for index, row in df.iterrows():
			if counter >0:
				if EMAIL == 'NULL':
					description =  row[int(DESCRIPTION)]
				else:
					description =  row[int(DESCRIPTION)] + '\nRaised by: '+row[int(EMAIL)]
				title = row[int(TITLE)]
				labels = [row[int(LABELS)]]
				date = parser.parse(row[int(CREATED_DT)]).isoformat()+'Z'
				__create_github_issue(title,description,date,labels,REPO_OWNER,REPO_NAME,TOKEN)
			counter = counter + 1
		return 1
	except Exception as e:
		print (e)
		return 0

#Internal function that creates the Issue creation request using Github's API v3
def __create_github_issue(title, body, date, labels,REPO_OWNER,REPO_NAME,TOKEN):
	url = 'https://api.github.com/repos/%s/%s/import/issues' % (REPO_OWNER, REPO_NAME)
	
	headers = {
		"Authorization": "token %s" % TOKEN,
		"Accept": "application/vnd.github.golden-comet-preview+json"
	}
	
	data = {'issue': {'title': title,
					'body': body,
					'created_at': date,
					'assignee': REPO_OWNER,
					'labels': labels}}

	payload = json.dumps(data)

	response = requests.request("POST", url, data=payload, headers=headers)
	if response.status_code == 202:
		print ('Successfully created Issue "%s"' % title)
	else:
		print ('Could not create Issue "%s"' % title)
		print ('Response:', response.content)
