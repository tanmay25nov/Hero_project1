from git import Repo
import github
repo = Repo ("D:\Git\Hero_project1")
head_commit = repo.head.commit
print(head_commit)
print(head_commit.author.name)
remote_repo = github.Repository('https://github.com/tanmay25nov/Hero_project1.git')
remote_commit_hash = remote_repo.get_commit("SHA").hexsha
print(remote_commit_hash)
#repo1 = Repo.clone_from("https://github.com/tanmay25nov/Hero_project1.git", ) 
# print(repo1.head.commit)