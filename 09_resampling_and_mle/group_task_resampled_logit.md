# Class Task: Logit with (re)sampled Data

One of the advantages of Big Data is that often one need only draw one (or multiple) large subsamples to get analytical results. How one samples data depends on the type of data one is analyzing and the question one is trying to answer.

For this task, we will be running a logit model to check for any evidence of imbalance. We will need a subsample of residential households from both the treatment and control groups, their pre-trial consumption data, and their pre-trail survey data.

## Set-Up
Download all the necessary files [**here**](https://www.dropbox.com/sh/j34pxsi8azvudvw/AABm6Syp2cnxyig6sO-qGNFia?dl=0). Password is the usual.

- `allocation_subsamp.csv` is a csv file with a subsample of IDs. It includes the IDs of:
	- control group (`tariff == 'E'`)
	- 4 treatment groups(`(tariff, stimulus) in {A, B} X {1,2}`)
- `kwh_redux_pretrail.csv` is a csv file with all the consumption data for the subsample above, including the time correction.
- `Smart meters Residential pre-trial survey data.csv` is a csv of the pretrial survey. The incredibly long and hideous codebook is available [**here**](https://www.dropbox.com/s/t7f3f1kzv0em34b/RESIDENTIAL%20PRE%20TRIAL%20SURVEY.doc?dl=0).

## The Task

2. create 5 unique vectors using the data from `allocation_subsamp.csv`
	- 1 with all the IDs of the control
	- 4 with the IDs of each different treatment
3. set the random seed to `1789` (doc [**here**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.seed.html))
3. use the function `np.random.choice` (doc [**here**](http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html)) and extract the following sample size *without replacement*:
	- 300 from the control group
	- 50 from treatment with tariff 'B'
	- 150 from treatment with tariff 'A'
4. create a `DataFrame` with all the the sampled IDs.
1. import the consumption data from `kwh_redux_pretrail.csv`
5. merge the consumption data with the sampled IDs, which will strip away a large portion of the original consumption dataframe.
6. aggregate all the consumption data **by month** for each **separate group**.
7. pivot the data from long to wide, so that `kwh` for each month is a variable.
8. merge the wide dataset with the treatment data.
9. compute a logit model comparing **each treatment group** to the control using only the consumption data.

## Group Assignment (may change)

Read `RESIDENTIAL PRE TRIAL SURVEY.doc`. Identify a few variables you think may be systematically different. Write up why you selected them.

`Smart meters Residential pre-trial survey data.csv`
