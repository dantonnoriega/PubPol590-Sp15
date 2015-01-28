#Intro to Pandas
**Part 2 -** Data Cleaning: Strings and missing values

---

We are going to jump straight into coding. It is best to learn by example and practice. Here is an outline of what we will cover:

### Outline

1. Python data types
	2. String: `str`, `unicode`
	3. Numeric: `int`, `float`, `long`
	4. Logical: `bool`
5. General tools for strings
	6. Converting case
		- `lower` and `upper`
	6. Splitting and joining
		- `split` and `join`
	7. Removing whitespace
		- `strip` `rstring` and `lstrip`
	8. Find if, and how many, characters or substrings exists within a string
		- `in`
		- `endswith` and `startswith`
		- `count`
	9. Find where characters or substrings are located within a string
		- `find` and `rfind`
		- `index`
	10. Replacing characters or substrings located within a string
		- `replace`
11. Regular Expressions (or regex) (aka "badass tools for strings")
	13. Syntax overview of regular expressions
		- pythex.org
	12. The `re` module
	13. Compiling a regular expression with `re.compile`
		14. Pattern matching
			- `findall`
		15. Substitution
			- `sub` and `subn`
		16. Splitting
			- `split`
17. Other methods for cleaning up vectorized strings in pandas
	- `cat`
	- `contains`
	- `count`
	- `get`
	- `len`
	- `pad`
	- `center`
	- `repeat`
5. Dealing with missing data
	6. option `na_values` within `read_table` and `read_csv` 

---

I will clarify after class with a follow-up on areas that we're confusing or lead to problems.
