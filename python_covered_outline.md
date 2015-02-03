# Python Topics Covered

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
8. Transforming, dropping, and imputing/replacing values


---

### Possible Topics
5. Date and Time
	- `datetime` module/toolkit
		- `datetime` `date` and `time` types
	- Methods
		- `year` `month` and `day`
		- `timedelta` 
5. General tools for strings
	- Converting case
		- `lower` and `upper`
	- Splitting and joining
		- `split` and `join`
	- Removing whitespace
		- `strip` `rstring` and `lstrip`
	- Find if, and how many, characters or substrings exists within a string
		- `in`
		- `endswith` and `startswith`
		- `count`
	- Find where characters or substrings are located within a string
		- `find` and `rfind`
		- `index`
	- Replacing characters or substrings located within a string
		- `replace`
17. Other methods for cleaning up vectorized strings in pandas
	- `cat` to concatenate
	- `contains` returns true if contains character or string
	- `count` returns a count of string occurrences
	- `get` to get element of a list by index value
	- `len`
	- `pad`
	- `center`
	- `repeat`
11. Regular Expressions (or regex) (aka "badass tools for strings")
	- Syntax overview of regular expressions
		- pythex.org
	- The `re` module
	- Compiling a regular expression with `re.compile`
		- Pattern matching
			- `findall`
		- Substitution
			- `sub` and `subn`
		- Splitting
			- `split`

