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

**IMPORTANT**: I intentionally *BIASED* the data used for these section. *The results here have no bearing on the real experiment.*

1. Download the file `task_4_kwh_w_dummies_wide.csv` [**here**][2]. Note that there is only ONE treatment group, `C4`. Also, note that a specific subset of dummy variables was pre-selected. The selected variables are listed in `RESIDENTIAL PRE TRIAL SURVEY_EDITED.docx` [**here**][2].
2. Repeat the procedure from Section 0.
	- Test for imbalance running Logit
	- Test for imbalance with a "Quick Means Comparison"
3. Answer the following questions in a separate document (.txt, .md preferred):
	1. Is there evidence of imbalance? Defend your claims by using the LOGIT output AND the Quick Means Comparison output.
	2. Compare what variables are considered significant (if any) in the Logit imbalance test versus the "Quick Means Comparison". Are the results different? If so, what do you think is driving the differences?
	3. Briefly explain the pros and cons of each imbalance check.

## Section 2: Propensity Score Weighting

We will producing the propensity score weights from page 4-10 of [Harding (2013)][harding].

#### Programming Note
The function `do_logit` returns an "regression results" object and the final dataframe used in the logit. Keep these results by assigning `do_logit()` to two variables, like `logit_results` and `df_logit`. For example,

```python
logit_results, df_logit = do_logit(df_pretrial, 'B', '3', add_D=None, mc=False)
```

1. Get the predicted values of the logit model ran in Section 1 using the `.predict()` method. Save them to a value, like `p_hat`.
	```python
	df_logit['p_val'] = logit_results.predict()
	```
	
2. Next, generate a column of weights called `w`. The formula for the weights is on page 4-10 from Harding (2013). Hints:
	- Generate a treatment variable. A quick way to do this is by using "boolean" vectors. Example: `df_logit['trt'] = 0 + (df_logit['tariff'] == 'C')` where `trt` here stands for Treatment (this is variable `D` in Harding 2013).
	- take the square root of elements within a vector (like a pandas column) by using `np.sqrt`. Example, the square root of all kwh consumption is `np.sqrt(df_logit['kwh']`).
	- review how the t-stats were generate "by hand" in section 0 to give you an idea of how to make a vector of weights `w` within the `df_logit` (or whatever you choose to call it) dataframe.
3. Create a smaller dataframe with just the IDs, treatments, and weights (e.g. `df_w = df_logit[['ID', 'trt', 'w']]`).

*Note:* if done correctly, this section should be very short. 


## Section 3: Fixed Effects with Weights

3. Import the file `task_4_kwh_long.csv` from [**here**][2].
4. Merge the smaller dataframe with the weights (`df_logit` in the section above) to the just-imported dataframe. Some observations will be lost -- this is alright.
5. Create a treatment and trial interaction variable (e.g. `df['trt_trial'] = df['trt']*df['trial']`).
5. Create a year-month variable, `ym`. All that is necessary is that `ym` be (1) a string variable and (2) uniquely distinguishes each year-month. An easy way to do this is to just convert the *year* and *month* variables into strings (e.g. `df['year'].astype(str)`) then concatenate  using `+`.
6. Create year-month dummy variable matrix. This is labeled `mu` in Allcott (2011) --- the seasonality controls. Use the `.iloc` method to omit the first variables to avoid the *dummy variable trap* (e.g. `pd.get_dummies(df['ym'], prefix = 'ym').iloc[:, 1:]`). Note that the first part,`[:,` means "take all rows"; the second part `, 1:]` means "columns from 1 to the end". More detailed info available on indexing [**here**](http://pandas.pydata.org/pandas-docs/version/0.15.2/indexing.html).

## Grading (TDB)

[1]: https://github.com/ultinomics/Duke_PUBPOL590/tree/master/10_fe_w_ps_weights "do_logit"
[2]: https://www.dropbox.com/sh/3yco7ur87mgpi3f/AACwUCRJ2_osUUClaVHK026la?dl=0 "task 4 dropbox"
[harding]: http://www.epri.com/abstracts/Pages/ProductAbstract.aspx?ProductId=000000003002001269 "harding"

[vid]: https://www.dropbox.com/sh/ccrvzpz5ynym5gn/AACV-MjrL9X01TSBkfLl3CQLa?dl=0 "quick_means"