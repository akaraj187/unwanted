import csv
from github import Github
g=Github()
repo = g.get_repo("ArduPilot/ardupilot")

open_issues = repo.get_issues(state='open',labels=['good first issue'])

with open('GF_issues.csv',mode='w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["sl.no","title","label","body"])


    i=1
    for issue in open_issues:
    
        #print(f"{i} {issue.title}")
        writer.writerow([i,issue.title,"good first issue",issue.body or " "])
        i=i+1
        if i > 10:
           break

print('Data Saved Succesfully')         
