# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OdbESKA0rCioS3ao17mdOt9kZsWSfn7n
"""

import re

# Define the regular expression pattern
pattern = r'a{3}'

# Input string
input_string = input("Enter a string: ")

# Use re.search to check if the input string contains exactly 3 consecutive 'a' characters
if re.search(pattern, input_string):
    print("The input contains exactly 3 consecutive 'a' characters.")
else:
    print("The input does not contain exactly 3 consecutive 'a' characters.")