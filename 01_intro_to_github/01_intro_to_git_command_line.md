<span style = "font-size: 170%">**PubPol 590** -- Workshop 1</span>

Intro to GitHub and Version Control
---

Whether you are working on your own project or on a team project, [version control](http://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) is essential. It's like using "track changes" in MS Word but cleaner and more dependable. It's also free, works on any operating system, and can track any text-like document -- not just a single MS word document. Most importantly, version control allows you to confidently and fearlessly get work done -- your own or your team's -- while avoiding file-clutter and file-renaming headaches. In short, you'll avoid this:

![phdcomics](https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/00_phd_comics_final_doc.gif)

In this class, we will be using a version control system called [Git](http://git-scm.com/) and a popular online repository hosting service called [GitHub](https://github.com/). GitHub is a powerful tool for building projects and collaborating with other researchers. To incentivize mastery of Git, any and all work for this class must be "pushed" to GitHub to receive credit.

Let's get started.  

---

**Objectives**
<!-- MarkdownTOC depth=2 -->

- Install GitHub and Git Bash
- Create A Github Account
- Git Command Line?
- Complete 15 minute Intro to Git
- Setting Up Git On Your Computer
- Learn Basic Unix Directory Commands
- Create a Local Repository and Push a Simple Text File to GitHub

<!-- /MarkdownTOC -->

---

## Install GitHub and Git Bash
### Mac OS X
1. [Install GitHub for Mac](https://mac.github.com/)
2. If you have OS 10.8 or below, then you'll need to install the Git [command line tools](https://github.com/blog/1510-installing-git-from-github-for-mac). Not necessary for Mavericks (10.9) and above.
3. Open the Terminal and check Git is installed by typing `git version`


### Windows
1. [Install GitHub for Windows](https://windows.github.com/)
2. GitHub should install Git Bash automatically

## Create A Github Account
1. Sign up for a [GitHub account](https://github.com/). *Make sure you use your __Duke__ email!*
2. Verify your email address. GitHub should send you an email automatically but if it does not, then follow [these instructions](https://help.github.com/articles/verifying-your-email-address/).
3. After you've verified your email, I *highly* recommend you request a [Student Developer Pack](https://education.github.com/pack). Hit "Get Your Pack" and follow the instructions. Getting your pack takes a few weeks but, once you get it, you'll be allowed 5 free private repositories for 2 years -- great deal!

## Git Command Line?
You may be wondering why I'm emphasizing Git command line after asking you to install the GitHub app. The GitHub app is user friendly with a wonderful graphic user interface (GUI). Git command line is looks scary and is very unpleasant for those not very comfortable with programming. 

However, it is very difficult to understand the machinery of what the GitHub app is doing without knowing basic Git command line. Furthermore, most firms use the GitHub app (or other [Git GUIs](http://git-scm.com/downloads/guis)) to "visualize" what is being done in the command line. The actual work of pushing/tracking files is generally not done on the GitHub app --- or any other Git GUI --- but via command line. Most importantly, if you learn Git using an specific Git GUI app, then you constrain yourself to knowing how to use Git *only* with that app. What if you switch to a firm or team that uses a different Git GUI? If you know Git command line, you can use *any* Git GUI.

I also want to introduce you all to what true programming feels like and that one need not be scared of command line interfaces. Command line coding is efficient and powerful but, yes, it can be scary. But just like any new skill, fear subsides with practice.

## Complete 15 minute Intro to Git 
GitHub has a great interactive introduction to Git command line. To familiarize yourself with how Git works, as well as the most frequently used commands, please take 15 minutes to run through [tryGit](https://try.github.io/levels/1/challenges/1).

You can find more detailed help about the basic Git commands being used [here](http://gitref.org/basic/).

## Setting Up Git On Your Computer

Before using Git, you need to configure a few things, like your `user.name` and `user.email`.

Here is what it looks like:
```
$ git config --global user.name "Danton Noriega (DUKE)"
$ git config --global user.email "drn12_at_duke.edu"
```

Just replace your own name and email for mine listed above.  

You can always check to see your global configurations running the following:
```
$ git config --global -l     # option -l stands for "list"
user.name=Danton Noriega (Duke)
user.email=drn12@duke.edu
color.ui=auto
core.editor=subl -n -w
```

## Learn Basic Unix Directory Commands  
Before we use Git locally on our own files, we should review a few Unix commands that are necessary for navigating through files and directories (aka the "file system") in the Terminal (Mac OS X) or Git Bash (Windows).

#### Basics 
`pwd` -- ("print working directory") this displays the current working directory
`cd` -- ("change diretory") is used to enter or exit (i.e. "change") directories. 
`ls` -- ("listing") will display all files and folders in the current working directory. You can use the option `-F` to distinguish directories (folders) from files and option `-a` to display *all* files and folders, even hidden ones.
`rm` -- ("remove") is used to delete files or folders. The system will not allow you to remove nonempty folders without a special option.
`mv` -- ("move") is used to move files into directories or to rename files.
`mkdir` -- ("make directory") creates a directory/folder

Also, for Mac OS X users, I recommend enabling [*tab completion*](http://www.ernieflores.net/osx-page-4/how-to-enable-tab-completion-in-mac-os-x-terminal/) in the Terminal. Git Bash enables tab completion by default so Windows users need not worry about enabling it. Tab completion takes some getting used to but it greatly speeds up writing command line code.

#### Example
Anything with a `$` first is an inputted command. Just below the command is the output (if produced). 
```
$ cd ~
$ pwd
/Users/dnoriega
$ ls
Applications        Documents       Google Drive        Pictures
Downloads       Library         Public
Box Sync        Dropbox         Movies          Samsung
Desktop         GitHub          Music           Sites
$ cd GitHub/
$ ls -F -a
./      ../     .DS_Store   PubPol590/
$ cd PubPol590/
$ ls -F -a
./      ../     .git/       .gitattributes
$ cd ..
$ pwd
/Users/dnoriega/GitHub2
```


## Create a Local Repository and Push a Simple Text File to GitHub
You are now going to put everything together and create a local repository.After that, you will create a matching online ("remote") repository on GitHub and then create, *stage*, *commit*, and *push* a simple text file from your local repo to GitHub.

#### 1. Create a Local Repository
Create a new folder on your computer that will house all your repositories. Name it something logical like "GitHub" or "Repositories". Let's assume you name it "GitHub". Next, go inside the folder and create another folder called "PubPol590". You can do this manually or using the Unix Command Line in the Terminal (Mac) or Git Bash (PC). In Unix command line, it would look something like this:  
    ```
    $ cd ~                      # change to home directory
    $ mkdir GitHub              # create directory "GitHub"
    $ cd GitHub                 # move inside "GitHub"
    $ mkdir PubPol590           # create directory "PubPol590"
    $ cd PubPol590              # move inside "PubPol590"
    ```

Go to your new folder "PubPol590" using Unix command line and initialize the repository.
    ```
    $ cd ~/Github/PubPol590/        # move inside "PubPol590"
    $ git init                      # initialize "PubPol590"
    ```

#### 2. Create an Online Repository on Github
[Login to your GitHub account](https://github.com/login). Make a new repository with the same name as your local repository (*PubPol590*):
    ![newrepo_gif](https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/new_github_repo.gif)

#### 3. Create a Simple Text File
Open up any text editor e.g. TextEdit (Mac) or Notepad (PC). Type in anything you'd like then save the file in your new repository, *PubPol590*.  For example:
    ![ultimate_gif](https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/ultimate_txt.gif)

#### 4. Add and Commit the File
First, check the status of your repo.
```
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    ultimate.txt
```

Git is letting us know that there is a file that has not yet been "staged". That is, the file has not been added to the list of changes we want to track. We can add ("stage") the files with the `$ git add [file_name]` then check the status again:
```
$ git add ultimate.txt
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    modified:   ultimate.txt
```

Next, we "commit" the changes to our staged files. We do this by using the `$ git commit -m "[write some text here]"` command. The option `-m` stands for message. Git will not allow you to commit files without a small commit message, so we use `-m` followed by short message in quotes to satisfy Git.

```
$ git commit -m "first commit"
[master f15b72e] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 ultimate.txt
```

Let's check the status of our repo one more time.
```
$ git status
On branch master
nothing to commit, working directory clean
```

Success! All our changes have been stored in our local repository. If we ever need to review our commits, we can use `$ git log` or, in a more condensed form, `$ git reflog`.
```
$ git log
commit f15b72e53b637d37c1ce53b52626faef78476670
Author: Danton Noriega (Duke) <drn12@duke.edu>
Date:   Sun Jan 11 22:38:21 2015 -0500

    first commit

$ git reflog
f15b72e HEAD@{0}: commit: first commit
```
All that is left for us to do is "push" our commits to our repo on GitHub.

#### 5. Push a Commit to GitHub
Go to your online repo on GitHub and copy the URL. Assuming you created the repo correctly, you should have a link that looks like `https://github.com/DRNoriega/PubPol590/` but with your GitHub username in place of `DRNoriega`. Make sure you're in your local repository and then run the following:
```
$ git remote add origin https://github.com/DRNoriega/PubPol590/
```

What Git is doing roughly translates to *"add the remote repository that is located at `https://github.com/DRNoriega/PubPol590/` and give it the local nickname `origin`"*. You can use any nickname but `origin` is the common choice for most programmers who use with git (I have no idea why).

Let's check to see that command ran successfully by using `$ git remote -v`. The option `-v` stands for "verbose". This will give us a list of the nicknames we have stored locally and the addresses they point to:
```
$ git remote -v
class   https://github.com/DRNoriega/PubPol590 (fetch)
class   https://github.com/DRNoriega/PubPol590 (push)
```

Everything looks good. The last step is to "push" our current commit. (We have yet to talk about "branching" but just know that the default nickname for any initial branch is `master`.)

Recall that the nickname for our remote repo is `origin`. The nickname of our local branch is `master`. Thefore, we want to "push" to `origin` the commits we have staged in `master`. 
```
$ git push -u origin master
Counting objects: 5, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 333 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/DRNoriega/PubPol590
   aadcb91..3306938  master -> master
Branch master set up to track remote branch master from origin.
```

Your output will likely be different from mine, but it gives you an idea of what to expect. Note the use of option `-u`. This option tells Git to remember where we are pushing to, and from where, so that next time we can just type `$ git push`.

#### 6. Verify Your Push
Let's verify that our push was successful.

Login to your GitHub account and go to your *PubPol590* repository. You should see something like this:
	![verify](https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/01/gifs/08_verify.gif)
	
If you see your file with the proper commit message, then success!

---

You now know the basics of Git. Next, you will learn how to use Git and GitHub to collaborate using the commands `fetch`, `merge`, and `pull`. You will also be shown how and when to use the commands `branch`, `checkout`, and `reset`.

