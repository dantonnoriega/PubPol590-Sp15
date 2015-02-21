# Group Task: Checking for Balance
#### Trim, Agg, and Plot

---


### DUE DATE is Wednesday 2/25 @ 3 pm
This is assignment is due before class next week -- **Wednesday 2/25 at 3 pm**.

## Checking For Balance

An important part of doing analysis of any Randomized Controlled Trail (RCT) is *checking for balance* (read Chapter 1 of Masters of Metrics for more details). If participants in an experiment were truly randomly assigned, then there should be no statistically significant difference in outcomes *before the treatment was implemented*. 

When dealing with observations over-time, checking for balance generally has a step where data is aggregated into longer time intervals (minutes/hours are aggregated to days or months). This is because it is unlikely that behavior for *any* household, regardless of assignment status, is similar from minute to minute or hour to hour. But over longer spans of time, trends appear and behavior will converge to a certain patter (thanks "law of large numbers").

Imagine to blizzard occurring at the same time but in different locations. Once snow storm drops on average 1 cm per hour, the other 1.1 cm. If you only compare how much snow falls hour to hour, ignoring what was accumulated before, it will be difficult to figure out which blizzard is dropping more snow. But if you sum up all the snow dropped over the entire day, it will be much more clear which blizzard was more powerful.

The CER data at the moment takes 30 minute smart meter readings. Comparing households at such small intervals will yield muddled results. But over the span of a day (or month) consumption behavior for a house will normalize to a distinguishable pattern. It is therefore incredibly important that we aggregate consumption data over longer time intervals.

For this task, we will be checking for balance using **daily** and **monthly** intervals.


## Task

Reproduce the following 2 graphs (does not have to be exactly the same -- the data should be close):

1. Monthly t-stats and p-values over-time
	![1][1]
2. Daily t-stats and p-values over-time
	![2][2]



## Algorithm Hints

How to aggregate:

1. Import and stack the entire data set (like in the last group task)
2. Merge and trim the data, keeping only *Residential Homes* that are in the *Control* or in the *Bi-Monthly Only Stimulus* and *Tariff A*.
3. Group and do a two sample t-test
4. Plot the t-values over time.


[1]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/06/06_monthly.png "monthly"
[2]: https://raw.githubusercontent.com/ultinomics/Duke_PUBPOL590/master/figs/06/06_daily.png "daily"

## Grading

To receive credit, you must push a folder with your python code and graphs to your team repo.

Criteria | 10 pts  	
--------------------------------|------
Concise and easy to read code 	|	**+1**  
Runs Out-of-the-Box				|	**+1**  
2 Correct Graphs *or*		 	| 	**+8**
Only 1 Correct Graphs 			|	**+6**






