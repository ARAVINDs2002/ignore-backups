# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xrYbW29cft6rQ83auRuLQDYOq_S0vuGF
"""

import re

text = "This is an example of SEO using regular expressions in Python. SEO is important for web optimization."
keyword = "SEO"

count = len(re.findall(keyword, text, re.IGNORECASE))
print(f"The keyword '{keyword}' appears {count} times in the text.")