import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



ds = pd.read_excel('HHD_C_Report_2022Q2.xlsx', sheet_name='Page 6 Data', index_col=0, header=(1,3))



print(ds.head)



#we will be using this for our trigometric function

#we can see some suprisinf numbers in 07 Q1 people who had a credit score UNDER 620 had originated 114 Billion$$ in mortage loans, while the next
# group people whose credit score was 620-659 had only 77 Billion$$ in mortage loan originations. 

# we can prob foretell a linear relationship of riskier loans/commodities and future bankruptcies/ US Fed Policy and Lobbying 

#Sinusoidal Regression Example
