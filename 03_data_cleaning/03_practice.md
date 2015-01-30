# 03 Online Demo
Missing and Duplicated Data

---

## Online Demos

[**Missing Data**](https://www.dropbox.com/s/zeny27nbipevlav/3_missing_data.mov?dl=0) online demo.  
[**Duplicated Data**](https://www.dropbox.com/s/1j10sk5zv82vynq/4_duplicated_data.mov?dl=0) online demo.

## Practice Cleaning Data

You are going to practice cleaning data with missing and duplicated values on the same small data set as before but with values removed (missing) and some duplicated.

Find the data [**here**](https://github.com/ultinomics/Duke_PUBPOL590/blob/master/03_data_cleaning/data/small_data_w_missing_duplicated.csv).

Your task is to do the following:

1. Convert any missing data to `NaN` values.  
	**HINT:** Import and inspect the data first then import the data again using the `na_values` option.
2. Drop (NOT PURGE) any FULL rows that are duplicated. That is, keep at least one occurrence of the duplicated rows, don't remove all of them (NOT PURGE!).
3. Find which rows of variable/column/Series `consump` are missing then extract the FULL rows from the dataframe. In short, look at the full rows of data where `consump` has missing data.
4. Check for any duplicated values on the SUBSET of `panid` and `date`. That is, search to see if any participant has duplicated dates. *Drop the rows where `consump` is missing for any duplicated values.*
5. Take the cleaned data set and then take the average (mean) of variable `consump`.  
	**HINT:** to find the overall mean of variable `panid` in DataFrame `df`, I would run `df['panid'].mean()` or `df.panid.mean()`



