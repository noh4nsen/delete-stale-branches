import os
from github import Github, Auth

github_token = os.environ['INPUT_TOKEN']
repo = os.environ['INPUT_REPOSITORY']

auth = Auth.Token(github_token)
github_instance = Github(auth=auth)

repo = github_instance.get_repo(repo)
branches = repo.get_branches()

qty_deleted_branches = 0

for branch in branches:
    if 'stale/' in branch.name:
        qty_deleted_branches += 1
        print("-- Deleting branch", branch.name, "--")
        ref = repo.get_git_ref(f"heads/{branch.name}")
        ref.delete()
print(f" \n-- {qty_deleted_branches} deleted branches --")