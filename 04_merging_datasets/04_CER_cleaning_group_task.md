# 04 Group Task
#### CER Data Cleaning and Merging

---

###UPDATE

Some videos covering advanced pathing and stacking are now available. There are two videos because I stopped one short by accident; [**Part 1**](https://www.dropbox.com/s/pntzg5tb54ip6oa/6_advanced_pathing_and_stacking.mov?dl=0) and [**Part 2**](https://www.dropbox.com/s/e0if1ecyzclrpph/6_advanced_pathing_and_stacking_2.mov?dl=0). These should help you with the group task. 

Remember, you need to download the files to get the full videos and the best quality.
 
You can also find the codes I practiced with and the codes from the video [**here**](https://github.com/ultinomics/Duke_PUBPOL590/tree/master/04_merging_datasets/codes). The folder *dans_practice* has what I did to teach myself and *online_demo* is what I did in the vid.
 
### DUE DATE is **Wednesday 2/11 at 3 pm**
This is assignment is due before class next week -- **Wednesday 2/11 at 3 pm**.

*EXTRA CREDIT* is available for teams who put in extra effort and time to load, clean, and explore the full data set -- not just the subset.

## Set-Up

Each group should have set up a team repository. 

**For your group to receive credit for this assignment, your group must:** 

1. Add me as a collaborator to the group repository on GitHub...
	2. Have the owner of the group repo go into the repo on GitHub.
	3. Click *Settings* on the right hand side.
	4. Under *Settings*, click on *Collaborators* on the left hand side.
	5. Please look for and add *DRNoriega*.

	Here is an example gif:  
	![add_collab](https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/04/add_collaborator.gif)
	
2. Each group must push their code to GitHub to receive credit for the assignment.

**NOTE:** I have *not* yet taught folks how to collaborate in groups on GitHub (aka [**GitHub Flow**](https://guides.github.com/introduction/flow/index.html)). Therefore, I *highly recommend* you work together, in-person, and have only *one* person pushing edits to the repo. Since you all have access to the repo, you will step on each others toes if you all work on the *same* file at the same time. This is possible once you learn how to *branch* and *merge* but that is something best learned together in class.

That said, you're more than welcome to work on *separate* files within the same repo, just as long as you make very clear which code is the one you want graded.

---

## Background

We know there are issues with the CER data. Before we can do any analysis, we need to fix them.

The known issues can be found [**here**](http://www.ucd.ie/issda/data/commissionforenergyregulationcer/).

## Group Task

Get into your groups and accomplish the following:

1. Download all the raw data [**here**](https://www.dropbox.com/sh/1srhgvqywye06a7/AACQ2j7r11wCfoY8HcpsHelfa?dl=0)
2. Import **part** (a subset) of the data
	- skip the first 6 million rows of each consumption data file and then import the next 1.5 million using the `read_table` options `skiprows` and `nrows`.

	Example: if I want to skip the first 100 rows of file `abc.txt` and then read the next 200 (so rows 101 to 301), I would write:
	```python
		pd.read_table('path/abc.txt', skiprows = 100, nrows = 200)
	```
3. Stack the data
	- **HINT**: After you stack the data, I recommend removing any of the old DataFrames you had using `del`. For example, if I stack `df1` and `df2`, I should then remove them using `del df1, df2`.
	
	```python
		df_stack = pd.concat([df1, df2], ignore_index = True)
		del df1, df2
	```
4. Clean the data
4. Merge the data

Yes, this is vague, but that's the point. It's an outline of what any researcher has to do given any new data set. 

It suppose to be challenging, so work in groups. I'll give you some video hints before the weekend. 

## Grading

Criteria | %  	
--------------------------------|------
Fixing errors listed in CER FAQ for the subset |	**80%** 
Concise and easy to read code 	|	**10%**  
Runs Out-of-the-Box				|	**10%**  

FYI, "Runs Out-of-the-Box" means that the code, after changing main directory and file paths, runs without any problems. In other words, if I have to debug your code (besides changing paths), you will lose 10% of your grade. 

The only thing worse than debugging your own code is debugging someone else's!

## Extra Credit (FULL DATA SET)

If you're patient and worked hard to import and explore the full data set, you can get extra credit.

Bonus | +%
------------|-------
Finding undocumented errors in the ENTIRE dataset | +**20%**

If you find any strange stuff in the entire data set that was not talked about the CER FAQ, you can get a 20% bonus to your grade.

