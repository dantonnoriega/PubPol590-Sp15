Group Task 4: Fixed Effects with Propensity Score Weighting
---

---

**DUE ON OR BEFORE APRIL 22nd @ 11:59 pm**

---

# Intro

Propensity score weighting can help remedy any bias due to non-random assignment  (see [Harding 2013][harding]). With such weights, we can get unbiased coefficient estimates in our regression model of choice.

In this task, we will be implementing the fixed effects model in [Allcott (2011)](https://files.nyu.edu/ha32/public/research/Allcott%202011%20JPubEc%20-%20Social%20Norms%20and%20Energy%20Conservation.pdf). Before doing so, we will review a quick way to check for imbalance if the results of a logit model are unclear.

## Section 0: Quick Means Comparison when Logit Check is Unclear

This section is **UNGRADED** but one must learn this part to do the next section.

1. Download `logit_functions.py` [**here**][1] and the practice data set `14_B3_EE_w_dummies.csv` [**here**][2]. Note that there is only ONE treatment group, `B3`.
2. Learn how to do a "Quick Means" comparison by watching the most recent video, `16_group_task_4_section_0.mp4`, [**here**][vid]. The video reviews:
	- how to make use of `logit_functions.py` by saving the file in the same folder as your code and then changing your working directory with `os.chdir`
	- using the `do_logit()` function
	- generate means for easy comparison using pandas methods `.groupby()` with `.mean()` and `.transpose()`.
	- quickly do a two-sample t-test "by hand" for *wide* data. If you forget the formula, it can be found in the appendix of Chapter 1 of *Mastering Metrics*, Harding 2013, or [wikipedia](http://en.wikipedia.org/wiki/Student%27s_t-test).

## Section 1: Finding Imbalance

>**IMPORTANT**: I intentionally *BIASED* the data used in sections 1-3. *Results in these sections have nothing to do with real CER experiment.*

1. Download the file `task_4_kwh_w_dummies_wide.csv` [**here**][2]. Note that there is only ONE treatment group, `C4`. Also, note that a specific subset of dummy variables was pre-selected. The selected variables are listed in `RESIDENTIAL PRE TRIAL SURVEY_EDITED.docx` [**here**][2].
2. Repeat the procedure from Section 0.
	- Test for imbalance running Logit
	- Test for imbalance with a "Quick Means Comparison"
3. **Answer the following questions in a separate document (.txt, .md preferred):**
	1. Is there evidence of imbalance? Defend your claims by using the LOGIT output AND the Quick Means Comparison output.
	2. Compare what variables are considered significant (if any) in the Logit imbalance test versus the "Quick Means Comparison". Are the results different? If so, what do you think is driving the differences?
	3. What do you think are the pros and cons of each imbalance check (Logit and Quick Means)?
	4. Comment on the survey questions selected. Are there any you think are irrelevant or redundant? What variables do you are missing but should have been included? Please be concise.

## Section 2: Propensity Score Weighting

We will producing the propensity score weights from page 4-10 of [Harding (2013)][harding].

---

#### Programming Note
The function `do_logit` returns an "regression results" object and the final dataframe used in the logit. Keep these results by assigning `do_logit()` to two variables, like `logit_results` and `df_logit`. For example,

```python
logit_results, df_logit = do_logit(df_pretrial, 'B', '3', add_D=None, mc=False)
```

---

1. Get the predicted values of the logit model ran in Section 1 using the `.predict()` method. Save them to a value, like `p_hat`.
	```python
	df_logit['p_val'] = logit_results.predict()
	```
	
2. Next, generate a column of weights called `w`. The formula for the weights is on page 4-10 from Harding (2013). Hints:
	- Generate a treatment variable. A quick way to do this is by using "boolean" vectors. Example: `df_logit['trt'] = 0 + (df_logit['tariff'] == 'C')` where `trt` here stands for Treatment (this is variable `D` in Harding 2013).
	- take the square root of elements within a vector (like a pandas column) by using `np.sqrt`. Example, the square root of all kwh consumption is `np.sqrt(df_logit['kwh']`).
	- review how the t-stats were generate "by hand" in section 0 to give you an idea of how to make a vector of weights `w` within the `df_logit` (or whatever you choose to call it) dataframe.
3. Create a smaller dataframe with just the IDs, treatments, and weights e.g. `df_w = df_logit[['ID', 'trt', 'w']]`.

>*Note:* if done correctly, this section should be very short. 


## Section 3: Fixed Effects with Weights

3. Save the file `fe_functions.py` to your working directory. Import the file `task_4_kwh_long.csv`. Both found [**here**][2]. Be sure to run `from fe_functions import *` so that you import the `demean` function.
4. Merge the smaller dataframe with the weights (`df_logit` in the section above) to the just-imported dataframe. Some observations will be lost -- this is alright.
5. Create the necessary variables:
	6. A treatment and trial interaction variable.
	7. Log of kwh consumption plus 1 e.g. `df['log_kwh'] = (df['kwh'] + 1).apply(np.log)`. The "plus 1" is to standard shift used to account for any consumption values that are equal to zero.
	5. Create a year-month column, `ym`. Example:
	```python
	# create month string `mo_str` that adds "0" to single digit integers
	df['mo_str'] = np.array(["0" + str(v) if v < 10 else str(v) for v in df['month']])
	# concatenate to make ym string values
	df['ym'] = df['year'].apply(str) + "_" + df['mo_str']
	```

7. Set up your regression variables from the merge dataframe:
	1. `y` = log of consumption
	2. `P` = pre-trial/trial indicator
	3. `TP` = treatment and trial period interaction
	4. `w` = weights variable e.g. `w = df['w']`
	2. `mu` = dummy variable matrix --- the seasonality controls. Use the `.iloc` method to omit the first column of dummies to avoid the *dummy variable trap* and the last column to reduce *multicollinearity* e.g. `	mu = pd.get_dummies(df['ym'], prefix = 'ym').iloc[:, 1:-1]`. Note that the first part,`[:,` means "take all rows"; the second part `, 1:-1]` means "from second column to the second-to-last". More detailed info available on indexing [**here**](http://pandas.pydata.org/pandas-docs/version/0.15.2/indexing.html).
	4. Concatenate `P`, `TP`, and `mu` into one dataframe called `X` e.g. `X = pd.concat([TP, P, mu], axis=1)`
6. De-mean `y` and `X` using the function `demean`
	7. Create a columns of IDs e.g. `ids = df['ID']`
	8. Demean `y` and `X` e.g. `y = demean(y, ids)`. Note that the first argument is the variable to demean and the second is the ID vector.
8. Run the Fixed Effects without AND with weights. *DO NOT add a constant!* (I made a mistake in the first FE codes I wrote a few weeks back):
	```python
	## WITHOUT WEIGHTS
	fe_model = sm.OLS(y, X) # linearly prob model
	fe_results = fe_model.fit() # get the fitted values
	print(fe_results.summary()) # print pretty results (no results given lack of obs)

	# WITH WEIGHTS
	## apply weights to data
	y = y*w # weight each y
	nms = X.columns.values # save column names
	X = np.array([x*w for k, x in X.iteritems()]) # weight each X value
	X = X.T # transpose (necessary as arrays create "row" vectors, not column)
	X = DataFrame(X, columns = nms) # update to dataframe; use original names

	fe_w_model = sm.OLS(y, X) # linearly prob model
	fe_w_results = fe_w_model.fit() # get the fitted values
	print(fe_w_results.summary()) # print pretty results (no results given lack of obs)
	```

9. **In a separate document, answer the following questions:**
>*NOTE*: fixed effect models with de-meaned values produces incorrect standard errors. They are smaller; sometimes by a lot. This produces large smaller p-values from a standard fixed effects model using dummies. For this exercise, pretend they are **correct**, and interpret accordingly. But, in the real world, know that one must fix the standard errors before believing any p-values. Remember, p-values aren't as important as many researchers think. That said, it's important to "speak the language" of academics, so might as well practice.
	10. Compare the coefficient estimates of the treatment-trial interaction variable. How did it change after using the weights?
	11. Interpret the coefficient estimate for the *first* regression *without* weights. If you were consulting CER on the effectiveness of the `C4` treatment, what would you conclude?
	11. Interpret the coefficient estimate for the *second* regression *with* weights. If you were consulting CER on the effectiveness of the `C4` treatment, what would you conclude?
	12. Do you think, given how biased the data was, that the weighted regression coefficient estimate on treatment-trial are believable? Please be concise.


## Grading

To receive credit, you must push a *folder* with your python code to your team repo. *Please CLEARLY identify which folder and files are to be graded!*

|Criteria 								| 	25 pts  	|
|---------------------------------------|---------------|
|Easy to read code 						|	**2**  		|
|Runs Out-of-the-Box					|	**3**		|
|**Section 1**                      	|  				|
|		 -- Well reasoned, concise responses to 4 prompts    | 	**8**	|
|**Section 2**                      	|  					|
|		 -- Generate correct weights		| 	**2**	|
|**Section 3**                      	|  					|
|		 -- Generate correct `y` and `X`		| 	**2**	|
|		 -- Well reasoned, concise responses to 4 prompts	| 	**8**	|


Long, incoherent responses will be *penalized*.

[1]: https://github.com/ultinomics/Duke_PUBPOL590/tree/master/10_fe_w_ps_weights "do_logit"
[2]: https://www.dropbox.com/sh/3yco7ur87mgpi3f/AACwUCRJ2_osUUClaVHK026la?dl=0 "task 4 dropbox"
[harding]: http://www.epri.com/abstracts/Pages/ProductAbstract.aspx?ProductId=000000003002001269 "harding"

[vid]: https://www.dropbox.com/sh/ccrvzpz5ynym5gn/AACV-MjrL9X01TSBkfLl3CQLa?dl=0 "quick_means"