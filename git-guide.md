# Project 0 - Git Guide  
## Command Line Git  
- status
	- Shows status of the local repository. This status includes:
		- number of local commits that have not been synced with remote (GitHub)
		- list of files in local folder that are NOT being tracked by git
		- list of files in local folder that have changes that need to be committed
	- `git status`
- clone
	- How you get the repository from the GitHub website to your local machine.
	- `git clone "whatever_the_url_from_github_is"`
- add
 	- This allows the user to add files for tracking by git.
 	- `git add file_name`
- rm
	- How to delete files from a git repository
	- `git rm file_name`
	- Can also be used to remove from tracking only
	- `git rm --cached file_name`
- commit
	- Creates a snapshot of changes to the files added using `git add`
	- use -m modifier to add the commit message in line instead of by prompt
	- `git commit -m "Commit message"`
- push
	- Used to send local commits to the remote repo
	- `git push`
- fetch
	- Lets the user take any differences from the remote repo that aren't in the local directory
	- `git fetch`
- merge
	- Used to put changes from one branch into another
	- `git merge <branch-name>`
- pull
	- Combination of `fetch` and `merge` commands, to update branches from the remote repo
	- `git pull`
- branch
	- How to list, create, or delete branches to your repo
	- DO NOT DELETE THE MAIN BRANCH
	- `git branch`
- checkout
	- How to switch branches in your git repo
	- `git checkout branch_name`
  
## git files & folders
- .git folder
	- The main identifier in a git repository that identifies it as a git repo
	- It also stores all of the code that allows git commands to work
- .gitignore file
	- A list of file names for git `status`, `add`, `commit`, etc to ignore
  
## GitHub
- Pull requests
- SSH authentication to repositories
	- How a user can access a remote repo from a local machine without a password

