# PubPol 590 -- Workshop 1
## GitHub and Version Control

Whether you are working on your own project or on a team project, [version control](http://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) is essential. It's like using "track changes" in MS Word but cleaner and more dependable. It's also free, works on any operating system, and can track any text-like document -- not just a single MS word document. Most importantly, version control allows you to confidently and fearlessly get work done -- your own or your team's -- while avoiding file-clutter and file-renaming headaches. In short, you'll avoid this:

![phdcomics](https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/Workshop%201/phd%20comics%20-%20final%20doc.gif)

In this class, we will be using a version control system called [Git](http://git-scm.com/) and a popular online repository hosting service called [GitHub](https://github.com/). GitHub is a powerful tool for building projects and collaborating with other researchers. To incentivize mastery of Git, any and all work for this class must be "pushed" to GitHub to receive credit.

Let's get started.  

---

**Objectives**
<!-- MarkdownTOC depth=0 -->

- Install GitHub and Git Bash
    - Mac OS X
    - Windows
- Create A Github Account
- 15 minute Intro to Git
- Basic Unix Directory Commands
- Using Git On A Local Repository
- Pull Then Push A File To The Class Repository

<!-- /MarkdownTOC -->

---

## Install GitHub and Git Bash
### Mac OS X
1. [Install GitHub for Mac](https://mac.github.com/)
2. Install the Git [command line tools](https://github.com/blog/1510-installing-git-from-github-for-mac)

### Windows
1. [Install GitHub for Windows](https://windows.github.com/)
2. GitHub should install Git Bash automatically

## Create A Github Account
1. Sign up for a [GitHub account](https://github.com/). *Make sure you use your __Duke__ email!*
2. Verify your email address. GitHub should send you an email automatically but if it does not, then follow [these instructions](https://help.github.com/articles/verifying-your-email-address/).
3. After you've verified your email, I *highly* recommend you request a [Student Developer Pack](https://education.github.com/pack). Hit "Get Your Pack" and follow the instructions. Getting your pack takes a few weeks but, once you get it, you'll be allowed 5 free private repositories for 2 years -- great deal!

## 15 minute Intro to Git 
GitHub has a great interactive introduction to Git command line. To familiarize yourself with how Git works, as well as the most frequently used commands, please take 15 minutes to run through [tryGit](https://try.github.io/levels/1/challenges/1).

You can find more detailed help about the basic Git commands being used [here](http://gitref.org/basic/).

## Basic Unix Directory Commands  
Before we use Git locally on our own files, we should review a few Unix commands that are necessary for navigating through files and directories (aka the "file system").

** Basics **
`pwd` -- ("print working directory") this displays the current working directory
`cd` -- ("change diretory") is used to enter or exit (i.e. "change") directories. 
`ls` -- ("listing") will display all files and folders in the current working directory. You can use the flag `-F` to distinguish directories (folders) from files and flag `-a` to display *all* files and folders, even hidden ones.
`rm` -- ("remove") is used to delete files or folders. The system will not allow you to remove nonempty folders without a special flag.
`mv` -- ("move") is used to move files into directories or to rename files.

Also, for Mac OS X users, I recommend learning how to use [Tab Completion](http://www.ernieflores.net/osx-page-4/how-to-enable-tab-completion-in-mac-os-x-terminal/). Git Bash enables Tab Completion by default so Windows users need not worry.

**Examples:**
Anything with a `$` first is an inputted command. Just below the command is the output, if any is produced. 
```
$ pwd
/Users/dnoriega
$ ls
Applications        Documents       Google Drive        Pictures
Downloads       Library         Public
Box Sync        Dropbox         Movies          Samsung
Desktop         GitHub          Music           Sites
$ cd GitHub/Duke_PUBPOL590/Workshop\ 1/
$ ls -F -a
./              .DS_Store           workshop_1.html
../             phd comics - final doc.gif  workshop_1.md
$ cd ..
$ ls -F -a
./      ../     .DS_Store   .git/       Workshop 1/
```

## Using Git On A Local Repository  
## Pull Then Push A File To The Class Repository  




