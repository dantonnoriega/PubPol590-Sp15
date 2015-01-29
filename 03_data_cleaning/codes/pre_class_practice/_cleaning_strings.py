import pandas as pd
import numpy as np

main_dir = "/Users/dnoriega/Desktop/pubpol590_data/"
git_dir = "/Users/dnoriega/GitHub/Duke_PUBPOL590/03_data_cleaning/"

# METHODS STRING --------------------------------

## create a sentence
sentence = "Data cleaning: a key hurdle to insight. Unforunate, but true"
type(sentence)

## 6. Converting case
##     - `lower` and `upper`
sentence.upper()
sentence.lower()

## 6. Splitting and joining
##     - `split` and `join`
sentence.split(' ')
sentence.split(',')
sentence.split(':')

list1 = sentence.split(' ')
'::'.join(list1)    # methods are part of objects. its not list1.join(' ') because `.join` is
                    # a method that is applied to string `str` types.
' '.join(list1)

## 7. Removing whitespace
##     - `strip` `rstring` and `lstrip`
word1 = "       boop       "
word1.strip()
word1.rstrip()
word1.lstrip()

## 8. Find if, and how many, characters or substrings exists within a string
##     - `in`
##     - `endswith` and `startswith`
##     - `count`
sentence3 = "na na na na na na na na, data! i mean, batman!"
'na' in sentence3
sentence3.endswith('na')
sentence3.startswith('na')

## 9. Find where characters or substrings are located within a string
##     - `find` and `rfind`
##     - `index`
sentence3.find('batman')
sentence3.rfind('na')
sentence3.find('superman')

## 10. Replacing characters or substrings located within a string
##     - `replace`
sentence3.replace('na', 'meow')