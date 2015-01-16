<span style = "font-size: 170%">**PubPol 590** -- Workshop 1</span>

Intro to GitHub and Version Control (OS X)
---

Whether you are working on your own project or on a team project, [version control](http://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) is essential. It's like using "track changes" in MS Word but cleaner and more dependable. It's also free, works on any operating system, and can track any text-like document -- not just a single MS word document. Most importantly, version control allows you to confidently and fearlessly get work done -- your own or your team's -- while avoiding file-clutter and file-renaming headaches. In short, you'll avoid this:

![phdcomics][00]

In this class, we will be using a version control system called [Git](http://git-scm.com/) and a popular online repository hosting service called [GitHub](https://github.com/). GitHub is a powerful tool for building projects and collaborating with other researchers. To incentivize mastery of GitHub, any and all work for this class must be "pushed" to GitHub to receive credit.

Let's get started.  

---

**Objectives**
<!-- MarkdownTOC depth=2 -->

- Install GitHub and Git Bash
- Create A Github Account
- Intro to the GitHub App

<!-- /MarkdownTOC -->

---

## Install GitHub and Git Bash
### Mac OS X
1. [Install GitHub for Mac](https://mac.github.com/)
2. If you have OS 10.8 or below, then you'll need to install the Git [command line tools](https://github.com/blog/1510-installing-git-from-github-for-mac). Not necessary for Mavericks (10.9) and above.
3. Open the Terminal and check Git is installed by typing `git version`

## Create A Github Account
1. Sign up for a [GitHub account](https://github.com/). *Make sure you use your __Duke__ email!*
2. Verify your email address. GitHub should send you an email automatically but if it does not, then follow [these instructions](https://help.github.com/articles/verifying-your-email-address/).
3. After you've verified your email, I *highly* recommend you request a [Student Developer Pack](https://education.github.com/pack). Hit "Get Your Pack" and follow the instructions. Getting your pack takes a few weeks but, once you get it, you'll be allowed 5 free private repositories for 2 years -- great deal!

## Intro to the GitHub App
The GitHub app is a graphic user interface (GUI) for Git, which is a command line program. We will be learning how to do version control using the GitHub app because it is user friendly and easier to learn.

That said, Git via command line is extremely powerful. However, it has a steeper learning curve and can be intimidating for new users who are not familiar with Unix command line. 

But the upside is that learning Git command line forces you to *understand* how Git works. It also means you can use Git on *any* computer and won't be constrained to having to use a specific GUI.

It's also more fun. You feel like a super bad ass hacker!

For my intro do Git command line, please go [**here**](https://github.com/ultinomics/Duke_PUBPOL590/blob/master/Workshop%201/01_intro_to_git_command_line.md)

Also, I will be using a lot of funny words. I'll explain them briefly as I go, but if you're ever lost or want more detail on some of the words, please refer to the [GitHub Glossary](https://help.github.com/articles/github-glossary/).


##### A Special Note About GitHub for Mac
Although very similar to the Windows version, the Mac and Windows version of the GitHub app has a few key differences. The biggest issue with GitHub for Mac is that you **cannot** revert to an old version using the app like you can on the Windows version. You have to use the command line on Mac. If something disastrous happens with your work and you use a Mac, come see me and I'll help teach you how to revert via command line.

### Create a Local Repository and Push a Simple Text File to GitHub
You are now going to create your first repository (aka "repo") and push your first file to GitHub!

#### Open the GitHub App and Login to Your GitHub Account
Open up the GitHub. It should be empty:

![fresh_github][01]
	
Go to *Preferences* and then *Accounts*. Input your username and password then sign in:

![preferences][02]

![accounts][03]


#### Create a Local Repository
Go to the the plus sign in the top left corner and select *create* and name a new repo. *"PubPol590"* is selected as the repo name in this example:

![name_repo][04]
	
Click the *"Changes"* tab. Notice that it's empty! This is because you have yet to add any files! Also, if you forget where your repo is, you can always right click the repo to find it on your hard drive:

![locate_repo][05]
	
#### Create a Simple Text File	
Open up any text editor e.g. TextEdit (Mac). Type in anything you'd like then save the file in your new repository:

![ultimate_gif][06]
    
Notice that under the changes that, it now has a file with a green *"NEW"*. The GitHub automatically detects any changes in a repo. In the right-most pane, it also gives a detailed view of exactly what has changed compared to any previous version.

#### Add/Stage and Commit the File
There are three places a file can be when inside a Git repo -- the **Working Copy**, the **Stage**, and the **Tree**. 

The **Working Copy** is just the file that exists, as is, inside the repo folder. It is the working copy of whatever file you are modifying.

The **Stage** is where one puts files that are tagged to be tracked. This isn't really a place as much as it is a tag. Some files are tagged to be tracked ("staged"), while other files are not. Files that are staged are then "committed" to the *Tree*. (A **commit** is a tracked and saved version of any and all files that were staged at the time of the commit.)

Lastly, the **Tree**. Inside each repo there is an invisible folder with the name *".git"*. This an invisible directory (or "tree") that houses every commit (or revision) ever submitted.

##### Add a File to the Stage aka "Staging"
GitHub automatically selects all files in the repo that have been added or modified in your repo. By selecting a file, you are telling GitHub that you would like to *"stage"* the file (i.e. add it to the files you want tracked). If you deselect a file, then GitHub will not stage the file and it will not be tracked.

##### Commit and Push
Once you've selected the files you want staged, you need to commit the files. When you commit files, you effectively save a copy of all stage files exactly as they are at the time of the commit. Who, what, when, and, if you're writing useful messages, *why* is recorded in every commit. This is what makes Git so useful!

Ok, let's commit the changes to your staged files. Note that GitHub will not allow you to commit files without a small commit summary. Add a brief summary. 

After you finish writing your summary, click the *Commit* button. Now that our files are locally committed, let's "push" those changes to a remote repo on GitHub accounts! To "push" the your commits, hit the *Publish* button in the top right corner. Note that this will only say "publish" the first first time you push a local repo that is not listed on your GitHub account. After you publish your repo on GitHub with your first push, the button will switch to saying "Sync".

![commit_push][07]
	
#### Verify Your Push
Let's verify that our push was successful.

Login to your GitHub account and go to your newly published repository. You should see something like this:

![verify][08]

![verify_png][09]
	
If you see your file with the proper commit message, then success!

---

You now know the basics of using the GitHub App.

[00]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/00_phd_comics_final_doc.gif "00_phd_comics_final_doc"
[01]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/01_fresh_github.png "01_fresh_github"
[02]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/02_preferences.png "02_preferences"
[03]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/03_login_info.png "03_login_info"
[04]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/04_name_repo.png "04_name_repo"
[05]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/05_locate_repo.gif "05_locate_repo"
[06]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/06_create_txt.gif "06_create_txt"
[07]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/07_commit_push.gif "07_commit_push"
[08]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/08_verify.gif "08_verify"
[09]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/09_verify.png "09_verify"

