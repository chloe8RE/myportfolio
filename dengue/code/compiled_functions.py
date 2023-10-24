#LIBRARIES
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import pickle

from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller  
import pmdarima as pm




#INSPECTION, DATA CLEANING

def data_inspect(df, df_name):
    print(f"{df_name} dataset inspection")
    print(f"--------------------------------------------------")
    print(df.info())
    print()
    print('++++++++++')
    print()
    print(f"Check for null percentages for {df_name} dataset:")
    null_percentages = (df.isnull().sum() / len(df)) * 100
    print(null_percentages)
    print()
    print('++++++++++')
    print()
    print(f"Check for no of duplicated values for {df_name} dataset:")
    print(df.duplicated().sum())
    print("++++++++++\n")

def shape_head(df, df_name):
    print(f"{df_name} dataset shape:")
    print(df.shape)
    print()
    print(f"{df_name} dataset head:")
    return df.head()




#EDA





# TIME SERIES MODELLING

def plot_traintest(y_train, y_test):
    plt.figure(figsize=(12,6))
    plt.plot(y_train, color='blue', label='y_train')
    plt.plot(y_test, color='orange', label='y_test')
    
    plt.title(label = "Plotting Train and Test Values", fontsize=12)
    plt.legend(fontsize = 9, loc = 'upper left'); 



def plot_forecast(y_train, y_test, arima_model, plot_title, X_test=None):
    # Generate len(y_test) number of predictions
    y_pred = arima_model.predict(n_periods = len(y_test), X=X_test) 
    
    plt.figure(figsize=(15,8))
    plt.plot(y_train, color='blue', label='y_train') #plot training data
    plt.plot(y_test, color='orange', label='y_test', alpha = 0.7) #plot testing data

    # Plot predicted test values. as shared previously, there are no index in y_pred 
    plt.plot(y_pred, color='green', label='y_pred', alpha = 0.9, ls = '--')
    
    # Find the MAPE (mean abs percentage error) of the predictions
    mape = mean_absolute_percentage_error(y_test, y_pred) 

    plt.title(label = f'{plot_title}\n MAPE: {mape:.2f}', fontsize=12)
    plt.legend(fontsize = 9, loc = 'upper left'); 