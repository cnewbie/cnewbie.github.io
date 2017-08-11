Title: Git Note
Tags: Git
#Git Note
##Git Basics
This chapter covers ervry basic command.
###Getting a Git Repository

Initialzing a Repository in an existing directory
>git init

Cloning an existing repository
>git clone [url]

###Recording Changes to the Repository
Checking the Status of Yours Files
>git status

Tracking New Files
>git add [filename]

Staging Modified Files
>git add [filename]

Short Status
>git status -s

Ignoring files
>.gitignore file save file patterns to match them.

The rules for the patterns you can put in the .gitignore file are as follows:
- Blank lines or lines starting with # are ignored.
- Standard glob patterns work.
- You can start patterns with a forward slash (/) to avoid recursivity.
- You can end patterns with a forward slash (/) to specify a directory.
- You can negate a pattern by starting it with an exclamation point (!).

Viewing Your Staged and Unstaged Changes
>git status & git diff
>git diff --staged  see what you've staged that will go into your next commit.
>git diff --cached see that you've statged so far.

Committing Your Changes
>git commit -m '' type commit message inline

Skipping the Staging Area
>git commit -a -m '' Git automatically stage every file that is already tracked before doing the commit,letting you skip the git add part.

Removing Files
>git rm remove file from your tracked files ,and also removes the file from your working directory.
>if you modified the file and added it to the index already,you must force the removal with the -f option.
>aanother userful thing you may want to do is to keep the file in your tree but remve it from your staging area.To do this ,use the --cached option.

Moving Files
>git mv [oldfilename] [newfilename]= mv [oldfilename] [newfilename]+git rm [newfilename]+git add [newfilename]

###Viewing the Commit History
By default,with no arguments,`git log` lists the commits made in that repository in reverse chronological order - that is ,the most recent commits show up first.
>git log -p -[number] shows the difference introduced in each commit.
>git log --stat shows some abbreviated stats for each commit.
>git log --pretty=[online,short,full,fuller,format] option 'format' which allows you to specify your own log output fotmat.[Userful options for git log --pretty=format](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History##pretty_format) & [Common option to git log](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History##log_options)

Limiting log Output
>git log -Sfunction_name [Options to limit the output of git log](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History##limit_options)

###Undoing Things
One of the common undos takes place when you commit too early and possibly forget to add some files or you mess up your commit message.if you want to try that commit again,you can run commit with the --amend ooption.
>git commit --amend This command takes your staging area and uses it for the commit.

Unstaging a Staged File
>git reset HEAD [filename] 

Unmodifying a Modified File
>git checkout -- [filename] 

###Working with Remotes
To be able to collaborate on any Git project,you need to know how to manage your remote repositories.

Showing Your Remotes 
>git remote -v shows you the URLs that git has stored for the shortname to be used when reading and writing to that remote.

Adding Remote Repositories 
>git remote add [shortname] [url]

Fetching and Pulling from your Remotes
>git fetch [remote-name]

Pushing to Your Remotes
>git push [remote-name] [branch-name]

Inspecting a Remote
>git remote show [remote-name] shows more information about a particular remote.

Removing and Renaming Remotes
>git remote rename [old-name] [new-name]
>git remote remove/rm [remote-name] remove a remote 

###Tagging
Git has the ability to tag specific points in history as being important.
Listing Your Tags
>git tag lists the tags in alphabetical order

Creating Tags
Git uses two main types of tags:lightweight and annotated.
A loghtweight tag is very much like a branch that doesn't change - it's just a pointer to a specific commit.
Annotated tags,however,are stored as full objects in the Git database.They're checksummed;contain the tagger name,email,and date;have a tagging message; and can be signed and verified with GNU Privacy Guard (GPG). 

Annotated Tags
>git tag -a [tagname] -m "message"

Lightweight Tags
>git tag [tagname] 

Tagging Later
>git tag -a [tagname] [sha1code]

Sharing Tags
>git push orign [tagname]
>git push orign --tags transger all of your tags to the remote server that are not already there.

Checking out Tags
git checkout -b [branchname] [tagname]

###Git Aliases
If you don't want to type the entire text of each of the Git commands,you can easily set up an alias for each command using `git config`.
>git config --global/local alias.[aliasname] [command]

##Git Branching
Branching means you diberge from the main line of development and continue to do work without messing with that main line.
###Branches in a Nutshell
When you make a commit, Git stores a commit object that contains a pointer to the snapshot of the content you staged.

Creating a New Branch
>git branch [branchname] create a new branch called testing.
>git log --oneline --decorate shows you where rhe branch pointers are pointing.

Switching Branches
>git checkout [branchname] this moves `HEAD` to point to the branch.
>git log --oneline --decorate --graph --all [Divergent history](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell#divergent_history)

###Basoc Branching and Merging

Basic Branching
>git checkout -b [branchname] switch branch
>git merge [branchname] merge branch 
>git branch -d [branchname] delete branch

Basic Merging
>git merge [branchname]

Basic Merge Conflicts
Occasionally,this process doesn't go smoothly.If you changed the same part of the same file differently in the two branches you're merging together.Git hasn’t automatically created a new merge commit. It has paused the process while you resolve the conflict. 

If you want to use a graphical tool to resolve these issues, you can run `git mergetool`.
>git mergetool [Advanced Merging](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging#_advanced_merging)

###Branch Management
The `git branch` command does more than just create and detele branches.
>git branch -v shows the last commit on each branch.
>git branch --mergen/nomerged filter this list to branches 
>git branch -d [branchname] detele the branch and lose that work.

###Branching Workflows
cover some common workflows that this lightweight branching makes possible.
[Brancheing Workflows](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)

###Remote Branches
Remote references are references in your remote repositories,includeing branches,tags,and so on.
you can get a full list of remote references explicitly with `git ls-remote [remote]` or `git remote show [remote] gor remote branches as well as more information.

Pushing
>git push [remote] [branch]/[localbranch]:[remotebranch]
The next time one of yoour collaborators fetches from the server.It's important to note that when you do a fetch that brings down new remote-tracking branches,you don't qutomatically have local,editable copies of them.

To merge this work into your current working branch,you can run `git merge origin/[branchmane]`.
>git checkout -b [branchname] orgin/[branchname] create local branch base on remote branch

Tracking Branches
>git checkout --track orgin/[branchname]

In fact,this is so common that there's even a shortcut for that shortcut.if the branch name you're trying to checkout doesn't exist add exactly matches a name on only one remote.Git will create a tracking branch for you.

If you already have a local brach and want to set it to a remote branch you just pulled down,or want to change the upsteam branch you're tracking.
>git branch -u origin/[branchname] 
>git branch -vv show what tracking branches you have set up.
>git fetch --all;git branch -vv fetch from all your remotes 

Pulling
>git pull

Deleting Remote Branches
>git push origin --delete [branchname] detele remote branch

###Rebasing
In Git, there are two main ways to integrate changes from one branch into another: the `merge` and the `rebase`.

The Basic Rebase
rebase a branch to master 
>git checkout [branchname]
>git rebase master
>git checkout master
>git merge [branchname]

There is no difference in the end product of the integration,but rebasing makes for a cleaner history.
Rebasing replays changes from one line of work onto another in the order they were introduced,whereas merging takes the endpoints and merges them together.

More Intersting Rebases
>git rebase --onto master [firstbranchname] [secondbranchname] 
Take the `second branch`forgure out the patches since it diverged from the `first branch`,and replay these patches in the `secondbranch` as if it was based directly off `master branch`instead. [A history with a topic branch off another topic branch](https://git-scm.com/book/en/v2/Git-Branching-Rebasing#rbdiag_e)

The Perils of Rebasing

Don not rebase commits that exist outside your repository
[Figure](https://git-scm.com/book/en/v2/Git-Branching-Rebasing#rbdiag_i)

Rebase vs. Merge
In general the way to get the best of both worlds is to rebase local changes you've made but haven't shared yet before you puch them in order to clean up your story,but never rebase anything you've pushed somewhere.

##Distributed Git
Git in a distributed environment as a contributor and an integretor.

###Distributed Workflows

Integration-Mannger Workflows
[Integration-Manager Workflow Figure](https://git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows#wfdiag_b)

To be continued