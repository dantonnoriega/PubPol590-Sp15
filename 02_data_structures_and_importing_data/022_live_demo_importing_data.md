
# LIVE DEMO
Data Structures and Importing and Exploring Data with pandas

---

### Overview
<!-- MarkdownTOC depth=4 -->

- Canopy: Python Scripts and IPython
- Initializing a Python Script
	- Setting The Main Directory and File Paths
		- Main Directory
		- File Paths
		- Example Of Assigning Paths To Variables
- How To Import Raw Data Into Pandas And Make A Dataframe
- Live Demo: Pandas, Part 1
	- Nuggets of Knowledge
	- The Live Demo
- Practice, Practice, Practice
- Assignment
- Learning More About pandas

<!-- /MarkdownTOC -->

---


## Canopy: Python Scripts and IPython

Open up Canopy, create a new *Editor Window* and then create a new file. You should now be able to type in the upper part of the window. Anything you write and save in the upper part will be saved as a **python script**, which is any file that contains the extension *.py*. Assuming no bugs or errors, these files can be executed by Python or an IDE that runs Python, like Canopy.

The lower part of the window is the **IPython Console**. **IPython** allows you to test any bit of Python code you like and provides immediate output. It also has numerous features that normal Python does not have. They are explained in detail in PDA but I will briefly preview the ones you will use the most:

1. **Tab Completion**. Anything that has been assigned a name in your session of Python (either by default, by a toolkit, or by the user) can potentially be completed by hitting the *tab* key. This greatly speeds up typing.
2. **Object Introspection** or "get info". You can get general info about an object or a function by using the question mark (?) before or after the object name. For example, to learn more about the `sum` function by typing `?sum` or `sum?`. If the source code of a function is available, you can see it by using two question marks (??).
3. **IPython Keyboard Shortcuts**. You should try to avoid using the mouse as much as possible. It's slow and clunky and makes you look like a noob. It is faster and more efficient to use the keyboard. Those milliseconds you save by using the keyboard add up overtime. Here is a list of keyboard shortcuts that speed up coding using IPython (this is part of Table 3-1 in PDA):
	```
	KEY 			BEHAVIOR
	up-arrow 		Search backward in command history
	down-arrow 		Search forward in command history
	Ctrl-A 			Move cursor to beginning of line
	Ctrl-E 			Move cursor to end of line
	Ctrl-K 			Delete text from cursor until end of line
	Ctrl-U 			Discard all text on current line
	Ctrl-F 			Move cursor forward one character
	Ctrl-B 			Move cursor back one character
	Ctrl-L 			Clear screen
	```
	
## Initializing a Python Script
The top of every one of your scripts will *always* have the following (the order of the lines doesn't matter):

```python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
```

To use any toolkit, like `pandas`, you have to import it. The line `import pandas as pd` tells Python that you want to import the toolkit `pandas` and that `pd` is how you will refer to any function from the pandas toolkit. Had you just written `import pandas`, you would have to write `pandas` whenever you used a pandas function. Therefore, the `as pd` of `import pandas as pd` sets us up to have to write less.

The line `import numpy as np` does the same thing for the NumPy toolkit.

The line `from pandas import Series, DataFrame` tells Python that you want to import the object creating functions _Series_ and _DataFrame_ and use them directly by name. Without this line, you would have to write `pd.Series`.

### Setting The Main Directory and File Paths

How you write code is important. For example, Google has an entire [style guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html) for how it's employees should be writing Python code.

One thing I am adamant about is making your code clean, readable, and, most important, easy to update.

The biggest culprit in violating clean, readable, and easy to update code is failing to set a main directory and file paths for your codes. Therefore, I'm **requiring** that all your codes have a *main directory path* assigned to a variable at the start of your code. I also recommend, but don't require, that any file you use have its paths to variables as well.

#### Main Directory
The **main directory** is generally the folder that contains the project you are working on. In this folder would be project codes, raw data, exported data, graphs etc. For example, the folder that contains all the stuff I develop for this class is called `Duke_PUBPOL590`. It's _**full system path**_ is `/Users/dnoriega/GitHub/Duke_PUBPOL590`. I would then assign this path to a variable. I generally use `main_dir`.

Visually, the main directory path `/Users/dnoriega/GitHub/Duke_PUBPOL590` looks like this...
![main_dir][main_dir]


#### File Paths
Next, the assignment of paths to any files you import or export along the way should also go at the top of your code. However, the paths should be _**relative to the main directory**_, not the system.

For example, I plan to load the file `sample_data_clean.csv`.

- The file's _**full system path**_ is `/Users/dnoriega/GitHub/Duke_PUBPOL590/02_data_structures_and_importing_data/data/sample_data_clean.csv`
- The file's _**relative path**_ is `/02_data_structures_and_importing_data/data/sample_data_clean.csv`
- Therefore, _**main directory path**_ + _**relative file path**_ = _**full system path of file**_  

Visually, the relative file path `/02_data_structures_and_importing_data/data/sample_data_clean.csv` looks like this...
![file_path][file_path]

#### Example Of Assigning Paths To Variables
So, what would this look like in a python script? Here is an example:

```python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590"
csv_file = "/02_data_structures_and_importing_data/data/sample_data_clean.csv"
```

**Notice the quotes around the paths.** This is critical. I'll explain more later but for now, just remember -- **_file paths must be in quotes!_**

## How To Import Raw Data Into Pandas And Make A Dataframe

The two pandas **import functions** that we will use the most in this class are `read_csv` and `read_table`. These functions read specific types of data files and import them as pandas *DataFrame*s. Another useful function we may use in this class is `read_excel`. When to use each of these function is described in the table below.

```
FUNCTION 		DESCRIPTION
read_csv 		Load delimited data from a file, URL, or file-like object. Use 
				 comma as default delimiter
read_table 		Load delimited data from a file, URL, or file-like object. Use
				 tab ('\t') as default delimiter
read_excel 		Load excel files (.xls, .xlsx)
```

More on how to use these in the live demo.

## Live Demo: Pandas, Part 1
Time for a live demonstration. Writing about code is much less effective then seeing code and its output done in real time.

### Nuggets of Knowledge
In this live demo, I will introduce the following nuggets of coding knowledge:

1. Variable assignment
2. Importing data using `read_csv`, `read_table`, and `read_excel`
3. Boolean (logical) operators and boolean comparison
4. Extracting data columns, rows
	5. extracting columns (Series) from a DataFrame using *attributes* versus *dict-like keys*
	6. extracting rows using slicing
	7. extracting rows using boolean indexing

### The Live Demo
Download the live demo I filmed [**here**][live_demo]. 

The file is large, 1.68 gigs. I did not upload it to youtube because the quality would suffer and the details matter. Also, my uploading it to YouTube would take longer than it would for you to download! 

You should be able to view it on Dropbox but the quality will be low. I recommend you download it on campus. The internet at Duke is (usually) very fast (at least it is in Gross Hall).

Use a top quality media player, like [**VLC**](http://www.videolan.org/vlc/download-macosx.html), that allows you to slow down the live demo if you find it too fast. Or you can just pause it.

(Keep in mind, this is the first live demo I've ever done so apologies if it is not very good.)

## Practice, Practice, Practice
The **ONLY** way to get better at coding is to practice. I'm not a hacker badass, to be honest. I'm just a guy who's done a LOT of coding in his life. I practice almost every day just through the work I have to do. So, practice!

## Assignment
To inspire you to practice (and to make up for lost time in class), here is your first assignment.

1. Download this [**data**][4] and unzip it. It is password protected. Please check the announcements on Sakai for the password.
2. Create a new python script and initialize it with the `import` etc. commands.
3. Assign the main directory and files to a path
4. Use the appropriate import function to import that data.
	6. **NOTE**: loading this data may take a bit depending on your computer. Be **patient**!
	5. **HINTS**: 
		- `read_csv(csv_file)` is equivalent to `read_table(csv_file, sep = ",")` where `sep` stands for separator. That is, we tell `read_table` that the delimiter (separator) is a commna.
		- `read_table(file)` by DEFAULT does `read_table(file, sep = "\t")`. The `\t` in `"\t"` is the python expression for *tab*. Therefore, the default is to use tab.
		- If the file pathed to `file` is NOT tab delimited, you need to tell the `read_table` function what the separator is. If the separator is a colon, it would be `read_table(file, sep = ":")`; if the separator is a space then it would be `read_table(file, sep = " ")` or, equivalently, `read_table(file, sep = "\s")` where `\s` is an expression for a space.
5. Extract rows **60 to 99** of the DataFrame using *row slicing*.
6. Extract all the rows where **electricity consumption** (kwh) is *greater than 30*.
7. Push your code to your personal class repo on GitHub.

Please try this on your own. The code should be VERY short. Struggle, sweat, and bleed before you give up and ask your teammates for help (or the answers)!

Good luck!

---

## Learning More About pandas 
[**Overview**][1] of what pandas was designed to do.  
[**10 min new user intro**][2] to pandas.  
Intro to pandas [**data structures**][3].  

[1]: http://pandas.pydata.org/pandas-docs/stable/index.html "index"   
[2]: http://pandas.pydata.org/pandas-docs/stable/10min.html "10min"  
[3]: http://pandas.pydata.org/pandas-docs/stable/dsintro.html "dsintro" 
[4]: https://www.dropbox.com/s/kc4pcnc780pqjk2/File1_small.txt?dl=0 "CERS"
[live_demo]: https://www.dropbox.com/s/bjtu7s6mahon8hl/pandas_part_1_live_demo.mov?dl=0 "live_demo"
[main_dir]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/02/main_dir.png "osx_file_path"
[file_path]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/02/file_path.png "osx_file_path"
