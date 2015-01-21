

---

<span style="font-size: 250%">**Intro to Pandas**</span>
<span style= "font-size: 170%">**Part 1 -** Data Structures and Importing Data</span>

---



You will spend most of this class learning to use **pandas**, a data analysis toolkit which allows one to quickly create, manipulate, and analyze data structures. Pandas has become an increasingly popular alternative to other free software programs like R (and many paid programs as well).

You will also see some references to a toolkit called **NumPy**. Pandas is built on top of NumPy, which a toolkit for doing quick computations using vectors and arrays. Data structures are just collections of vectors and arrays, which is why NumPy forms the foundation of pandas.

Let's get started.

---
### Topics
<!-- MarkdownTOC depth=4 -->

- Understanding the Data Structures of pandas
- Before Importing: Understanding Raw Data
	- File Paths
	- File Type and Delimiters
	- File Size

<!-- /MarkdownTOC -->

---

## Understanding the Data Structures of pandas
The two data structures objects in pandas that you will learn to use are _**Series**_ and _**DataFrame**_.

A _Series_ object is analogous to a single column of data in an Excel spreadsheet. Like an Excel column, a _Series_ object has two components, _data_ and an _index_. In Excel, each cell of a column has a row index _(i.e. Column A, Row 1 = Cell A1)_. This is the same with a _Series_ object, except you can change the name of the index to anything you want while in Excel, the row numbers (index) are always positive integers.

A _DataFrame_ object can be thought of a collection of equal-length _Series_ objects. It would be analogous to a spreadsheet in an Excel workbook with more than two equal length columns of data. Just like with any column of an Excel spreadsheet, you can reference or extract any column of data in a _DataFrame_ as a _Series_ object. Any collection of two or more equal length _Series_ objects is considered a _DataFrame_; any collection two or more equal length columns of data in an excel spreadsheet imported to pandas would qualify as a _DataFrame_.

This will make more sense once you start using pandas.

## Before Importing: Understanding Raw Data
Before we jump into learning about pandas, it's best to go over a few things about raw data files. 

Importing data into pandas requires that you know 4 things about a raw data file:

3. **path** *e.g.* `/Users/[username]/Desktop` (Mac) or `C:\\Users\[username]\` (PC)
1. **type** *e.g.* CSV file or XLS file 
2. **delimiter** *e.g.* is it a comma, tab, space, etc. separating columns of data. This is generally a function of the file **type**.
4. **size** *e.g.* 25 kb or 200 mb or 2 gb)

If you know these 4 things about your file, then it is rather straight-forward to import data. However, each can also cause headaches for new programmers.

#### File Paths
Computers are organized by directories (folders) and files. Each directory and file on a computer has a path that allows it to be located by your operating system. 

Finding the path to a file is generally the first major headache programmers have to deal with when importing data. It can be tricky to find the path of a file or a directory. Here are some tips:

##### Mac

1. Open up the app *TextEdit*. If a new text window doesn't open automatically, then go to *File>>New* or just hit *command + n*.
2. Convert the file to plain text by going to *Format>>Make Plain Text* or just hit *command + shift + t*.
3. Find the file or folder you need to path. Drag and drop it onto the window. It will automatically give you the path written as text.
4. Copy and then paste the path wherever.

![osx_file_path][osx_file_path]
##### PC

1. Locate the file or folder.
2. Hold *shift* and right-click the file or folder you need to path.
3. Select the option *copy as path* (or something like that).
4. Paste wherever needed.

Moving forward, if you ever need to find the path of a file, you can use this tricks to get it quickly!

###### A Special Note About Pathing In Mac Versus PC

Paths are different for Mac and PC. For Macs, paths are joined by forward slashes (`/`). For PC, it is backslashes (`\`). Also, in PC, paths must start with the drive name followed by a `:\\` *e.g.* `C:\\` or `D:\\`.

#### File Type and Delimiters
The extension of a file tells us the file type. The file type will often also tell us what the delimiter is. The most common universal text file types for sharing small to moderately sized files are *CSV* and *TXT* files.

CSV stands for *comma separated values* and has extension *.csv*. This is the go-to file type for sharing data. It is the most compatible file type and less prone to parsing errors (parsing is when a computer processes text).

TXT stands for *text* and has the extension *.txt*. Usually, text files with data that end with *.txt* are either *tab-delimited* or *space-delimited* files. The columns are separated by tabs or spaces (or just whitespace).

However, this is not always the case. A *.txt* file can have any type of text data using any kind of delimiter. I've seen semicolons used as well as double colons (`::`). These odd delimiters can often lead to problems when attempting to import data but most import functions can handle such curve-balls.

Other popular file types that are not text files and DO NOT have text delimiters:
```
		TYPE 			PROGRAM
		.xls, .xlsx		Excel
		.dta 			Stata
		.sas7bat 		SAS
		.db 			SQL
```

Other than the Excel files types, we will generally stick to CSV and TXT files.

#### File Size
Big Data is a reference to the sheer size of modern data. However, in this class, we will not be able to do any work with actual Big Data. This is because none of our laptops could handle it!

In fact, most desktop and laptops struggle with even relatively small data sets. For example, importing a text file that is 2 gb large can take some computers a very long time. And 2 gb is nothing! Most applications, like Excel or Notepad, generally crash when opening CSV files that are over 1 gb.

This is why computer scientist create databases. For example, SQL or Microsoft Access are popular database management system. For even larger databases that need to be spread across many computers, large firms will use management systems like HaDoop or MangoDB.

In this class, we will stick to files that are less than 500 mb in size. This can still be a lot for some computers, especially older ones. The initial import can take some time, making your computer max out its processors and seem like its frozen. Fortunately, once imported by pandas, things tend to smooth out.

---

Next, we'll do a live demonstration.