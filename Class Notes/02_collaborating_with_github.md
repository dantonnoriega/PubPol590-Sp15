<span style = "font-size: 170%">**PubPol 590** --- Workshop 1</span>

Collaborating with GitHub
===

I can't imagine working on my own solo projects without Git and GitHub. I can work from any computer, track all of my work, and experiment without messing up working versions of my code. However, the real reason GitHub was created was for programmers to collaborate en masse. ["Open source"](http://opensource.org/) software, for example, is built by community of coders who collaborate to improve the same program. This ability for anyone to contribute and improve source code is not new (e.g. [Sourceforge](http://sourceforge.net/) has been around since 1999), but it has been significantly democratized by platform such as GitHub.

Coding is no longer just for hackers and CS majors. Nowadays most academic research includes a significant programming component. In order to increase productivity --- and to make research open and reproducible --- thousands of academic teams have adopted version control software like GitHub for collaborating. (For a great overview and guide to best practices in empirical social science, see [Gentzkow and Shapiro][1].)

In this class, we will try to emulate start-ups and top academic researchers by learning to collaborate on projects using GitHub. You will each be part of a team. As a team, you will learn to code together, honing your skills on your group project so you can then do data analysis solo for your individual project.

No one truly codes alone. Coders congregate online to ask for help and share tips. [StackExchange](http://stackexchange.com/tour), for example, has numerous communities devoted to programming. One of the most popular --- and my personal go-to --- is [Stack Overflow](http://stackoverflow.com/). But if you're looking for help that is *project specific*, [Googling](http://lmgtfy.com/) for help or turning to Stack Overflow often isn't option. Perhaps your problem is specific to your proprietary data or you're getting funny results. Those are problems best left to you and your team to solve --- with the internet as a reference tool.

[GitHub Flow](https://guides.github.com/introduction/flow/index.html) "branch-based" workflow will be the method each team will learn to help facilitate collaboration. As a class (and hopefully within your teams), we will incorporate aspects of the [Agile Development Philosophy ](http://en.wikipedia.org/wiki/Agile_software_development#Agile_principles) by coding in groups and breaking down projects into smaller deliverables that are turned in every two weeks.

Understanding GitHub Flow will require that we learn about *"branching"*. Specifically, we will learn how to manage and use branches by *"checking out"*, *"fetching"*, *"merging"*, and *"pulling"* branches. Since mistakes are inevitable, we will also learn how to *"reset"* a branch.

Let's get started.

[1]: http://www.brown.edu/Research/Shapiro/pdfs/CodeAndData.pdf "Gentzkow and Shapiro (2014)"

----

**Objectives**

<!-- MarkdownTOC -->

- Cat Teams
- Create a Team Repo and Add Collaborators
- GitHub Workflow
- Practice

<!-- /MarkdownTOC -->

----

## Cat Teams
1. **Break up into teams.** 
	
	Yes, we know --- it's the first day, it's awkward, and you have no idea if your new teammates will be burdens or all-stars or somewhere in between. Welcome to the real world.

	Each team will be named after a type of cat. Henceforth, your *"Cat Team"*.

2. **Write the name, duke email, and GitHub username of each team member on your Cat Team sheet.** Turn them in to me *at the end of class* so I have a record of who is on what team and what your GitHub usernames are.

## Create a Team Repo and Add Collaborators
1. **Select ONE person to [create a new team repo on GitHub](https://help.github.com/articles/create-a-repo/)**. It can be anyone but recognize that the person who creates the repo will have a few extra privileges --- like deleting it! Worry not, you can always transfer ownership of a repository to another teammate. Everyone else will be added as collaborators. For an overview of all of this, go [**here**](https://help.github.com/articles/permission-levels-for-a-user-account-repository/).
2. **Have the owner of the team repo [add the rest of the team as collaborators](https://help.github.com/articles/adding-collaborators-to-a-personal-repository/)**. Note that you must enter the GitHub usernames of your teammates, not emails.

You're good to go! You can now start collaborating! So, let's learn what that means.

## GitHub Workflow

To understand how [GitHub Workflow](https://guides.github.com/introduction/flow/index.html), one must understand what a *branch* is and what it means to *branch out*.

### Branch
From the GitHub [Glossary](https://help.github.com/articles/github-glossary/):
>A branch is a parallel version of a repository. It is contained within the repository, but does not affect the primary or master branch allowing you to work freely without disrupting the "live" version. When you've made the changes you want to make, you can merge your branch back into the master branch to publish your changes.

[*Branching out*](https://help.github.com/articles/branching-out/) is therefore the process of creating a branch of the master branch.

### Why is this Useful?
It may be hard to see at the moment, but once we begin programming in Python, it will become more apparent, especially once we learn how to make functions.

Here is a real world example from my own work:
>I have a function that imports data from a spreadsheet into Python, cleans the data, and then returns the cleaned dataframe. I would like to poke around and explore the data. This means writing new functions that create tables, histogram, graphs, etc. So, I make a branch for each new function: `make_tables`, `make_histograms`, and `plot_trends`.

>However, if I had a team, I could assign each new function as a task to a teammate. Each teammate can work away on their branch at the same time until they have a working version or hit a wall. In either case, they can submit a "[pull request](https://help.github.com/articles/using-pull-requests/)". The team can discuss the code in the branch, test it out, and even modify it. Once the branch has been fixed up and is working well, it can be merged to the master branch. Throughout the process, the entire team will have a record of what is being done, why, and how. This helps the entire team become better programmers.

### Shared Repo Model
There are [two types of collaborative development models](https://help.github.com/articles/using-pull-requests/) that make use of *pull requests*. Given the size of our teams, We will be using the *shared repository model*.

## Practice
Alright, time to practice!









