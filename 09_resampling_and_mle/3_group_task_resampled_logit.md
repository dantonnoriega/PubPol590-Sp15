# Group Task 3: Logit with Resampled Data

---

**DUE APRIL 8TH BEFORE CLASS (3:05 pm)**

---

One of the advantages of Big Data is that often one need only draw one (or multiple) large subsamples to get analytical results. How one samples data depends on the type of data one is analyzing and the question one is trying to answer.

For this task, we will use the logit model to check for any evidence of imbalance. To reduce computation costs/time, we will use a subsample of residential households from both the treatment and control groups.

## Set-Up
Download all the necessary files [**here**](https://www.dropbox.com/sh/j34pxsi8azvudvw/AABm6Syp2cnxyig6sO-qGNFia?dl=0). Password is the usual.

- `allocation_subsamp.csv` is a csv file with a subsample of IDs. It includes the IDs of:
	- control group (`tariff == 'E'`)
	- 4 treatment groups(`(tariff, stimulus) in {A, B} X {1,3}`)
- `kwh_redux_pretrial.csv` is a csv file with all the consumption data for the subsample above, including the time correction.
- `Smart meters Residential pre-trial survey data.csv` is a csv of the pretrial survey. The incredibly long and hideous codebook is available [**here**](https://www.dropbox.com/s/t7f3f1kzv0em34b/RESIDENTIAL%20PRE%20TRIAL%20SURVEY.doc?dl=0).
- `data_section2.csv` is a finished wide data set required for generate results in Section II.

---

## The Task

The task starts in class. Teams must finish *both sections* by the due date.

### Section I: Resampled Logit, Consumption Only (started in-class March 25)

**HINTS AVAILABLE [HERE](https://www.dropbox.com/sh/ccrvzpz5ynym5gn/AACV-MjrL9X01TSBkfLl3CQLa?dl=0)!** Video is `14_group_task_3_hints_sect1`

2. create 5 unique vectors using the data from `allocation_subsamp.csv`
	- 1 with all the IDs of the control
	- 4 with the IDs of each different treatment
3. set the random seed to `1789` (doc [**here**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html))
3. use the function `np.random.choice` (doc [**here**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html)) and extract the following sample size *without replacement*: (**THE ORDER MATTERS**)
	1. 300 from the control group
	4. 150 each from treatment (A, 1)
	5. 150 each from treatment  (A, 3)
	2. 50 each from treatment (B, 1)
	3. 50 each from treatment (B, 3)
4. create a `DataFrame` with all the sampled IDs.
1. import the consumption data from `kwh_redux_pretrial.csv`
5. merge the consumption data with the sampled IDs, which will strip away a large portion of the original consumption dataframe.
6. compute aggregate **monthly** consumption for each panel ID.
7. pivot the data from long to wide, so that variable `kwh_[month]` exists for each different `[month]`.
8. merge the wide dataset with the allocation data from `allocation_subsamp.csv`.
9. compute a logit model comparing **each treatment group** to the control (4 logit models total) using only the consumption data as independent variables.

### Section II: Logit with Survey Data

3. Watch the [tutorial video](https://www.dropbox.com/sh/ccrvzpz5ynym5gn/AACV-MjrL9X01TSBkfLl3CQLa?dl=0) on how to use the code.
2. Download the [following code](https://github.com/ultinomics/Duke_PUBPOL590/blob/master/09_resampling_and_mle/task_3_hints/09_group_task_3_section_2.py).
1. Review how the survey questions were coded by reading `RESIDENTIAL PRE TRIAL SURVEY.doc`.
2. Select **2 QUALITATIVE Questions** (i.e. categorical variables) BESIDES `Question 200` (gender) to use in the logit models. *NOTE: Rows with ANY missing data will be removed automatically.* Preference more complete questions as it will keep more IDs.
4. Compute a logit model comparing **each treatment group** to the control using consumption data AND the question dummy variables. Do this using function `do_logit`. *Try to choose question where the logit function **converges***.
5. **In a separate document** (MS Word, .docx, is ok; markdown, .md, is preferred), **please do the following**: 
	5. Briefly explain the results of each different logit regression with the 3 variables you selected (which converge). Highlight any significant differences between the models and if there is any evidence of imbalance. Please be concise.
	6. Briefly explain the benefit(s) and potential problem(s) of using ALL the available survey variables in a logit regression. Please be concise.
	7. Briefly explain when and why (if at all) it would be sufficient to use only a subset of the available survey questions. Please be concise.

## Grading

To receive credit, you must push a *folder* with your python code to your team repo. *Please CLEARLY identify which folder and files are to be graded!*

|Criteria 								| 	10 pts  	|
|---------------------------------------|---------------|
|Easy to read code 						|	**1**  		|
|Runs Out-of-the-Box					|	**2**		|
|**Section 1**                      	|  				|
|		 -- Proper Random Sampling Order| 	**2**		|
|		 -- Correct Logit Results		| 	**2**		|
|**Section 2**                      	|  					|
|		 -- Well reasoned, concise responses to 3 prompts		| 	**3**|

Long, incoherent responses will be *penalized*.
