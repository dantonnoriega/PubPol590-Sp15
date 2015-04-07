# Python Topics Covered

*Students will not be expect to learn anything more advance than what is listed above. Codes for more complicated operations, like what is require to do Fixed Effects models (covered at the end of class), will be provided.*

### Outline

1. Intro to Pandas
	- DataFrames and Series
	- Importing data
		+ `read_csv`
		+ `read_table` and option `sep`
	- Extracting data
		- Row slicing and boolean indexing
		- Single and multiple columns
	- File paths
1. Python data types
	- String: `str`, `unicode`
	- Numeric: `int`, `float`, `long`
	- Logical: `bool`
5. List and tuples
	- `append` and `extend`
	- `len` function
	- converting to `Series` or `DataFrame`
		- `zip` function
		- `dict` notation
		- `concat` pandas module for Series to DataFrame
2. Iterating over values
	- `for` loops
	- `print` function
	- one-line `for` loops
	- `enumerate` for objects
	- `iteritems` module for Series and DataFrame
5. Dealing with missing data
	- Option `na_values` within `read_table` and `read_csv`
	- Missing data types
		- null/missing values (`NaN`) aka "not a number"
		- pandas `isnull` to find missing values (also `np.isnan`)
		- pandas `notnull` to find non missing values
	- Filling in and Dropping missing values
		- `fillna`
		- `dropna`
7. Finding duplicate values
	- `duplicated` to find duplicated values
		- option for duplicated `take_last` i.e. `df.duplicated(take_last = True)` 
	- `drop_duplicates` for dropping duplicates
7. Copying data sets with `copy`
8. Replacing values
	- `replace` to replace values
	- `map` to replace values
9. Merging and Concatenating Data
	- `pandas.merge()` to merge data
		+ options `on`
		- options `how = 'inner'` and `how = 'outer'`
			+ `'inner'` a merge using the intersection
			+ `'outer'` is a merge using with the union
	+ `pandas.concat()` to column or row bind data sets
		+ options `axis = 0` to row bind and `axis = 1` to column bind
10. Grouping Data (aka Split-Apply-Combine)
	- `.grouby()` method to group data (groups store index values of dataframe)
		+ `.sum()` method to get sum values for each groups
		+ similarly `.mean()`, `.std()`, and `.count()`
		+ `.groups` method to extract a dictionary object of values (WARNING: Do NOT CALL DIRECTLY -- can crash python)
			* `.groups.keys()` to see all the keys (aka groups)
			* `.groups.iteritems()` to iterate through key-index combinations
		+ `.get_group()` method to get a specific group given key value
11. Plotting Values
	- importing `matplotlib.pyplot` (aka `plt`) package for simple plots
		+ `plt.figure()`  to initialize plot object
		+ `.sub_plot()` to add a subplot
		+ `.plot()` to plot
10. Pivoting (Reshaping) Data
	- `.pivot` to take 'long' form (panel) data to 'wide'
	- use of `.reset_index(inplace=True)` to extract index as a variable
11. Intro to Regression using package `statsmodels.api` (`sm`)
	- setting up variables (dependent `y` and independent variables `X`)
	- `sm.OLS` and `sm.Logit` model-objects
	- `.fit()` method for model-objects to generate estimates
	- `.summary()` of fitted model to get results
