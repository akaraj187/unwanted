from github import Github
g=Github()
repo = g.get_repo("ArduPilot/ardupilot")
open_issues = repo.get_issues(state='open',labels=['good first issue'])
i=1
for issue in open_issues:
    
      print(f"{i} {issue.title}")
      i=i+1
      if i > 10:
         break
