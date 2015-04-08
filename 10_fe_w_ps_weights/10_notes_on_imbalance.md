# Notes on Group Task 3: Testing for Imbalance Using Logit

We have covered 2 ways of testing for imbalance in this class. The first was doing a two sample t-test (via plotting) to check for significant differences in consumption overtime (daily and monthly). The second---covered in group task 3---was using a logit model to find significant predictors---a sign of imbalance. 

The second method (using logit) is, theoretically, the faster and easier way to check for imbalance across multiple variables. It is not necessary to plot a graph for each different variable. One can simply throw variables into the logit model and check to see if anything is significant. But in practice things are rarely so simple.

There is another method, which we did not technically cover---a *simple means comparison*. This is *NOT* the same as a two sample t-test because it does not test for significance. It is a quick "first step" to check for problems. For example, if it the means are almost the same for a variable across different assignments, then one can likely skip testing for imbalance. But if they do seem to be quite different, then one could verify that the difference is statistically significant via a two sample t-test. Likewise, if one is testing for imbalance using a logit model and no variables are significant, one can can do a means comparison to check if the insignificance is due to multicollinearity (more on this later) or proper random-assignment.

In group task 3, it was hopefully noticed that variables in a model---particularly dummy variables---can often be problematic. Two common headaches are **perfect separation** (aka "perfect prediction") and **multicollinearity**. Deep understanding of these two topics is best left to an Econometrics course, but it is important to understand the general concept. *(You are expect to understand these issues in practice but will not be expected to know the technical details.)*

## Perfect Separation

*Perfect separation* is occurs when an independent variable perfectly predicts either a "success" (e.g. assigned to treatment) or a "failure" (e.g. being assign to control). A coefficient estimate for such a variable cannot be calculated because there is no variation in the variable across the two possible outcome values. In a sense, there is no need to estimate a coefficient if perfect separation exists: if a variable perfectly predicts a success or failure, then, based on the data, one knows the outcome with 100% certainty.

The issue of *perfect separation* can be solved in three ways:

1. *Adding more data or having lots of data to begin with.* (preferred)
2. *Create a new category that merges an infrequent category with a more frequent one.* For example, instead of having 10 age categories of 10 years (Age 0-9, 10-19, 20-29 etc.) it is common practice to merge less common age groups into one large category (Age 0-18, 19-30, 30-40, 41-65, 65+). One can imagine that the dummy variable in the 90-99 range starts to get very sparse!
2. *Removing the offending variable (column removal) and any offending rows of said variable (row removal).*

Perfect separation occurs much more often in smaller data sets. In the real world, the relationship between data and some binary outcome variable is rarely perfectly predictable. There is randomness and noise. Therefore, by adding/getting more data, one increasing the probability of getting variation in the independent variables across both outcomes of the dependent (binary) variable.

One is more likely to encounter perfect separation with independent dummy variables that with continuous variables. "Sparse" Dummy variables---dummies with few 1s and many, many 0s---can very easily cause perfect separation. All the ones just need to align perfectly with either all 0 outcomes or 1 outcomes. Therefore, when possible, categories that will produce sparse dummy variables should be avoided or merged into another more general category. Again, this becomes less of an issue when one has access to lots of data.

If one does not have access to more data or cannot combine categories, then the last-resort method is to remove the offending variable and any offending observations so that the model can be estimated. This, however, can cause a "spiral of death" of sorts: by removing rows of data, one loses data, which *increases* the chance of perfect separation occurring in other previously non-offending variables.

Removing offending variables is the approach the algorithm takes in group task 3. If one puts in many, many dummy variables into the logit, one is sure, given the few hundred rows of data and many sparse categories, to find variables with perfect separation. As the model removes these offending variables and rows, it will then likely find other variables that also cause perfect separation, removing even more columns and rows, etc. until there is little data left to estimate anything at all!

The better approach here would be to use all of the available data instead of drawing such small subsamples from each assignment group (recall that some were as small as 50!).

## Multicollinearity

Multicollinearity is when one or more variables are highly correlated with one another. In the worst case, one has *perfect* multicollinearity. This is when any independent variable can be written as a linear combination of other independent variables. The *Dummy Variable Trap* is an example of perfect multicollinearity. *Perfect Multicollinearity is a violation of the ordinary least squares assumption* and it is solved by removing the offending variable.

The other kind is *high* or *imperfect* multicollinearity. This is when two or more variables are very highly correlated but not perfectly. *This is **NOT** a violation of the ordinary least squares assumption.* Coefficient estimates, assuming a model is correctly specified (i.e. no endogeneity), would still be *unbiased*. The problem, however, is that high multicollinearity "blows up" standard errors. Large standard errors means that t-values will be small; no variables will be found significant in the model. For prediction or propensity score matching, this is not an issue, as we do not care about the significance of the independent variables. But when checking for imbalance via logit, high multicollinearity is an annoyance because we *do* care about the significance.

If one is checking for imbalance with a logit model and finds evidence of high multicollinearity (e.g. ridiculously large standard errors) then there is another easy way to test for imbalance without having to make loads of graphs: a simple means comparison *without testing for significance*. This can be done quickly and easily using the `.groupby()` and `.mean()` (or `.agg()`) methods in `pandas`. Plotting mean-values is also much easier than plotting t-stats or p-values. (I will show you an example in class.)

It is important to clarify that this is not that same as a two sample t-test, which does check for significance (the more complicated thing we plotted in group task 2). A two sample t-test checks to see if two sample come from two different distribution by comparing means. It is possible to have different means but, given the large variation in data, one *fails to reject* that the each sample comes from a different distribution. The two sample could have come from the same distribution but just seemed distinct by chance.


