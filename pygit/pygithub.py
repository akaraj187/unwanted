import csv
from github import Github
g=Github()
repo = g.get_repo("ArduPilot/ardupilot")
#i will write all issues by labelling non 'good first issues' as 'hard'
all_issues = repo.get_issues(state='open')

with open('all_issues.csv',mode='w',newline='',encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["sl.no","title","label","body"])


    i=1
    for issue in all_issues:
          is_hard=True

          for label in issue.labels:
              if label.name =='good first issue':
                writer.writerow([i,issue.title,"good first issue",issue.body or " "])
                is_hard =False
                break

          if is_hard:
            writer.writerow([i,issue.title,"Hard",issue.body or" "])
          i=i+1
          if i > 100:
           break

print('Data Saved Succesfully')         
