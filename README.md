# Python_Analytics

A model set for pandas, seaborn, and numpy



----- we will also be using this for stocks analysis on pricing and predictive measures in the coming days

---- for the first analysis ----
Our explanatory variables in this model strategy are the moving averages for past 3 days and 9 days for the stock price. 

Remember that when you have more empty variables in a list you increase away from a point, and you begin to mess with limits (calculus fun)

so we will be using the dropna() function and store the feature variables in X.

we will be using the sklearn.linear_model, importing its LinearRegression function,
our accuracy for NSRGY (Nestlé S.A.) is 96.64% correct to using this model, as time goes on I will add to this, evenatually using other models.

Linear Regression Model - NSGRY accuracy = 96.64% 

Linear Regression Model - CPB accuracy = 90.62% (notice the change in confidence/accurancy, we use a notable time frame difference in the CPB example)

Linear Regression Model - SPY accuracy = 95.62% 

Linear Regression Model - Netflix accuracy = 98.75%

Linear Regression Model - META accuracy = 97.96%

Our second type of analysis will be a time series approach, with the Prophet package in Python we can model in using its cross validation function to measure forecasting error using historical data. Or a fancy way of saying we want to be able to better predict the future. 

