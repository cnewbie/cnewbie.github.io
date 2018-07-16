Title: Git Cheatsheet
Tags: Git
lang: zh
Summary: Git 命令速查  
Date: 2018-07-14  
Modified: 2018-07-16  

---
title: Git Cheatsheet

---

-----------------------------

# Git 基础

## 基础操作  

初始化仓库  

`git init`  
`git clone [url]`  

检查文件状态  

`git status`  

跟踪文件  

`git add [file name]` 跟踪新文件/暂存已修改文件  

对比文件修改内容  

`git diff [file name]`  
`git diff --cached/staged [file name]` 对比暂存区文件  

提交更新  

`git commit`  
`git commit -m [message]`  更新纪录  
`git commit -a -m [message]`  跳过暂存文件步骤直接提交  

移除文件  

`git rm [file name]` 删除文件并取消跟踪  
`git rm --cached [file name]` 取消跟踪文件  

重命名文件  

`git mv [file name]`  

```bash
mv old_name new_name
git rm old_name
git add new_name
```

查看提交历史  

`git log` [git log](https://git-scm.com/docs/git-log)   
`git log --pretty=format: "%h %s" --graph`  

撤销提交  

`git commmit --amend`  
`git rebase -i` 

撤销暂存文件  

`git reset HEAD [file name]`   
`git reset --hard [file name]` 当前文件修改丢失  

撤销文件修改  

`git checkout -- [file name]`   

## 远程仓库  

查看远程仓库  

`git remote -v` 

添加远程仓库  

`git remote add [short name] [url]`   

从远程仓库获取文件  

`git fetch [remote name]`  

推送到远程分支   

`git push [remote name] [branch name]`  

查看远程仓库  

`git remote show [remote-name]`  

远程仓库重命名   

`git remote rename [old name] [new name]`  

删除远程仓库  

`git rm [remote name]`  

## 标签  

查看标签  

`git tag`  

添加附注标签  

`git tag -a [tag name] -m [message]`   

查看标签详情  

`git show [tag name]`  

添加轻量标签  

`git tag [tag name]`  

推送标签至远程服务器  

`git push [remote branch name] [tag name]`  

推送所有标签  

`git push [remote branch name] --tags`  

特定标签上建立分支  

`git checkout -b [branch name] [tag name]`  

# Git 分支  

## 分支基本操作

分支创建  

`git branch [branch name]`  

分支切换  

`git checkout [branch name]`  

查看分支历史  

`git log --oneline --decorate --graph --all`  

合并分支  

`git merge [branch name]`  

删除分支  

`git branch -d [branch name]`  

## 远程分支

查看远程分支  

`git ls-remote` or `git remote show [remote name]`  

推送分支  

`git push [remote] [local branch]  == git push [remote] [local branch:remote branch name]`  

跟踪分支  

`git chenckout -b [branch] [remote name]/[branch]`  

设置上游分支  

`git branch -u [remote name]/[branch]`  

查看跟踪分支  

`git branch -vv`  

抓取分支更新  

`git fetch --all`  

删除远程分支  

`git push [remote] --delete [branch name]` or `git push [remote] :[branch naem]`  

[example](https://git-scm.com/docs/git-push#_examples)  

分支合并  

`git rebase/merge`  
`rebase`历史纪录更简洁  [变基](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)  





# Git 工具  

引用日志  

查看分支引用的历史纪录  
`git reflog`  

提交区间  

双点语法,查看后者引用中特定的提交  

`git log [ref name1]..[ref name2]`  

多点语法,不包含最后引用的提交  

`git log refA refB ^refC == git log refA refB --not refC`  

三点语法,查看两引用的差异提交  

`git log [ref name1]...[ref name2]`  

## 储藏与清理  

储藏工作空间  

`git stash save`  

查看储藏列表  

`git stash list`  

应用储藏  

`git stash apply [ref]`  

删除储藏  

`git stash drop [ref]`  

不储藏暂存区文件  

`git stash save --kep-index`  

应用储藏包括暂存区  

`git stash apply --index`  

储藏包含未跟踪的文件  

`git stash -u/--include-untracked`  

新建分支并应用储藏  

`git stash branch [nranch name]`  

移除为跟踪文件  

`git clean`  

移除所用文件并储藏  

`git stash --all`  

## 重写历史  

修改最后一次提交  

`git commit --amend`  

交互式修改ref开始的所有提交  

`git rebase -i [ref]`  

批量修改提交  

`git filter-branch --tree-filter [command] [ref]`  

切换根目录  

`git filter-branch --subdirectory-filter [directory name] [ref]`  

## 重置对比  

相反操作操作提交指针  

`git reset --soft HEAD~  |  git commit`  

相反操作暂存区  

`git reset [file name]  |  git add [file name]`  

撤销所有修改包括工作区  

`git reset --hard HEAD~`  

恢复暂存区文件版本其他不变  [精简历史](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified#Squashing)  

`git reset [ref] -- [file name]`  

切换HEAD指针不丢弃工作目录修改  

`git checkout [branch name]`  

丢弃文件修改  [reset,checkout,revert](https://github.com/geeeeeeeeek/git-recipes/wiki/5.2-%E4%BB%A3%E7%A0%81%E5%9B%9E%E6%BB%9A%EF%BC%9AReset%E3%80%81Checkout%E3%80%81Revert-%E7%9A%84%E9%80%89%E6%8B%A9)  

`git checkout -- [file name]`  

## 子模块  

添加子模块  

`git submodule add  [url]`  

抓取后初始化模块  

`git submodule init`  

抓取后更新子模块  

`git submodule update --remote`  

查看子模块日志  

`git log -p --submodule`  

更新合并  

`git submodule update --remote --merge/--rebase`  

检查子模块是否推送  

`git push --recurse-submodules=check`  

批量操作子模块  

`git submodule foreach [command]`  
