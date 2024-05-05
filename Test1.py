from git import Repo
repo = git.repo("https://github.com/tanmay25nov/Hero_project1.git”)
head_commit = repo.head.commit
print(head_commit)

for commit in repo.iter_commits():
    commit_id = commit.hexsha
    print(commit_id)