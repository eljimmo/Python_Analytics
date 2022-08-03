import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


ds = pd.read_excel('HHD_C_Report_2022Q2.xlsx', sheet_name='Page 29 Data', index_col=0, header=3)


print(ds.head)

# overall while delinquencies are up from recent times, they are still way below regular rates for all age groups 
