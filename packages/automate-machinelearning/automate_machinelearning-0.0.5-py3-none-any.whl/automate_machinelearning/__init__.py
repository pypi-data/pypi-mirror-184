#!/usr/bin/env python
# coding: utf-8

# In[1]:


def data_summary(data):
    
    """The function data_summary() is used to provide a basic details of the 
       given tabular dataset.
       
       data_summary(data) function contains one argument.
       
       data -> We need to pass the entire dataframe to this function. (type = dataframe)
       
       Example: data_summary(data = dataframe_name)"""
    
    import pandas as pd
    import numpy as np
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame:
        
        print('*' * round(data.shape[1] / 2) + " "+"Top five rows in the data" + " "+'*' * round(data.shape[1] / 2))
        display(data.head())
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Last five rows in the data" + " "+'*' * round(data.shape[1] / 2))
        display(data.tail())
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Column present in the data" + " "+'*' * round(data.shape[1] / 2))
        display(list(data.columns))
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Number of rows and columns in the data" + " "+'*' * round(data.shape[1] / 2))
        print("Number of observation present in the data are {}.".format(data.shape[0]))
        print("Number of columns present in the data are {}.".format(data.shape[1]))
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Numerical columns in the data" + " "+'*' * round(data.shape[1] / 2))
        if len(list(data.select_dtypes(exclude=['object', 'category', 'datetime64']).columns)) > 0:
            display(list(data.select_dtypes(exclude=['object', 'category', 'datetime64']).columns))
            print("Number of numerical columns present in the data are {}.".format(len(list(data.select_dtypes(exclude=['object', 'category', 'datetime64']).columns))))
        else:
            print("There are no numerical columns present in the data.")
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Categorical columns in the data" + " "+'*' * round(data.shape[1] / 2)) 
        if len(list(data.select_dtypes(include=['object', 'category']).columns)) > 0:
            display(list(data.select_dtypes(include=['object', 'category']).columns))
            print("Number of categorical columns present in the data are {}.".format(len(list(data.select_dtypes(include=['object', 'category']).columns))))
        else:
            print("There are no categrical columns present in the data.")
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Date columns in the data" + " "+'*' * round(data.shape[1] / 2)) 
        if len(list(data.select_dtypes(include=['datetime64']).columns)) > 0:
            display(list(data.select_dtypes(include=['datetime64']).columns))
            print("Number of date and time columns present in the data are {}.".format(len(list(data.select_dtypes(include=['datetime64']).columns))))
        else:
            print("There are no date and time columns present in the data.")
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Information about the data" + " "+'*' * round(data.shape[1] / 2))
        data.info()
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Numerical description in the data" + " "+'*' * round(data.shape[1] / 2))
        if len(list(data.select_dtypes(exclude=['object', 'category']).columns)) > 0:
            display(data.describe())
            print()
        else:
            print("No numerical column is available for description")
        
        print('*' * round(data.shape[1] / 2) + " "+"Categrical description in the data" + " "+'*' * round(data.shape[1] / 2))
        if len(list(data.select_dtypes(include=['object', 'category']).columns)) > 0:
            display(data[list(data.select_dtypes(include=['object', 'category']).columns)].describe())
            print()
        else:
            print("No categorical column is available for description")
        
        print('*' * round(data.shape[1] / 2) + " "+"Null values present in the data" + " "+'*' * round(data.shape[1] / 2))
        display(data.isna().sum().sort_values(ascending=False))
        print("Total number of null values present in the given data is {}.".format(data.isna().sum().sum()))
        print()
        
        print('*' * round(data.shape[1] / 2) + " "+"Unique values in categrical data" + " "+'*' * round(data.shape[1] / 2))
        categorical_data = list(data.select_dtypes(include=['object', 'category']).columns)
        if len(categorical_data) > 0:
            
            for i in categorical_data:
                print("The total number of unique values present in {} is {}.".format(i, data[i].nunique()))
                unique_data = list(data[i].unique())
                if np.nan in unique_data:
                    unique_data.remove(np.nan)
                print("The unique values are: {}.".format(unique_data))
                print()
        else:
            
            print("No categorical data present.")
        
    else:
        
        print("The given data is not a dataframe.")


# In[2]:


def data_eda(data, target_column_name, regression):
    
    """The function data_eda() is used to provide a basic exploratory data analysis of the 
       given tabular dataset using matplotlib and seaborn library.
       
       data_eda(data, target_column_name, ml_type) function contains three argument.
       
       data -> We need to pass the entire dataframe to this function. (type = dataframe)
       target_column_name -> We need to pass the column name of the target variable (y). (type = string)
       regression -> We need to pass the supervised learning type based on the target_column_name. (type = bool)
                   True -> target_column is numerical.
                   False -> target_column is discrete or categorical.
       
       Example: data_eda(data = dataframe_name, target_column_name = column_name, regression = True)
                data_eda(data = dataframe_name, target_column_name = column_name, regression = False)"""
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame:
        data_numerical = list(data.select_dtypes(exclude=['object', 'category', 'datetime64']).columns)
        numerical_data = []
        discrete_data = []
        categorical_data = list(data.select_dtypes(include=['object', 'category']).columns)
        for i in data_numerical:
            if data[i].nunique() > 20:
                numerical_data.append(i)
        for i in data_numerical:
            if i not in numerical_data:
                discrete_data.append(i)
        
        print('*' * round(data.shape[1] / 2) + " "+"Univariate Analysis" + " "+'*' * round(data.shape[1] / 2))
        if len(numerical_data) > 0:
            print('*' * round(data.shape[1] / 2) + " "+"Univariate Analysis on numerical data using histogram" + " "+'*' * round(data.shape[1] / 2))
            for i in numerical_data:
                plt.figure(figsize=(12, 8))
                plt.title("Histogram for {}.".format(i))
                sns.histplot(data[i])
                plt.show()
            print()
            
            print('*' * round(data.shape[1] / 2) + " "+"Univariate Analysis on numerical data using boxplot" + " "+'*' * round(data.shape[1] / 2))
            for i in numerical_data:
                plt.figure(figsize=(12, 8))
                plt.title("Boxplot for {}.".format(i))
                sns.boxplot(data[i])
                plt.show()
            print()    
        else:
            print("There are no numerical data present in the given data.")
            print()
            
        if len(discrete_data) > 0:
            print('*' * round(data.shape[1] / 2) + " "+"Univariate Analysis on discrete data using countplot" + " "+'*' * round(data.shape[1] / 2))
            for i in discrete_data:
                plt.figure(figsize=(12, 8))
                plt.title("Countplot for {}.".format(i))
                sns.countplot(data[i])
                plt.show()
            print()
        else:
            print("There are no discrete data present in the given data.")
            print()
            
        if len(categorical_data) > 0:
            print('*' * round(data.shape[1] / 2) + " "+"Univariate Analysis on categorical data using countplot" + " "+'*' * round(data.shape[1] / 2))
            for i in categorical_data:
                plt.figure(figsize=(12, 8))
                plt.title("Countplot for {}.".format(i))
                sns.countplot(data[i])
                plt.show()
            print()
        else:
            print("There are no categorical data present in the given data.")
            print()
            
        print('*' * round(data.shape[1] / 2) + " "+"Bivariate Analysis" + " "+'*' * round(data.shape[1] / 2))
        if regression == True and type(target_column_name) == str and target_column_name in numerical_data:
            print('*' * round(data.shape[1] / 2) + " "+"Bivariate Analysis on numerical data" + " "+'*' * round(data.shape[1] / 2))
            if len(numerical_data) > 0:
                for i in numerical_data:
                    if i != target_column_name and len(numerical_data) > 2:
                        plt.figure(figsize=(12, 8))
                        plt.title("Scatterplot between {} and {}.".format(i, target_column_name))
                        sns.scatterplot(x=i, y=target_column_name, data=data)
                        plt.show()
                print()            
            else:
                print("There are no numerical data present in the given data.")
                print()
                
            print('*' * round(data.shape[1] / 2) + " "+"Bivariate Analysis on discrete data" + " "+'*' * round(data.shape[1] / 2))
            if len(discrete_data) > 0:
                for i in discrete_data:
                    if i != target_column_name: 
                        plt.figure(figsize=(12, 8))
                        plt.title("Boxplot between {} and {}.".format(i, target_column_name))
                        sns.boxplot(x=i, y=target_column_name, data=data)
                        plt.show()
                print()            
            else:
                print("There are no discrete data present in the given data.")
                print()
                
            print('*' * round(data.shape[1] / 2) + " "+"Bivariate Analysis on categorical data" + " "+'*' * round(data.shape[1] / 2))
            if len(categorical_data) > 0:
                for i in categorical_data:
                    if i != target_column_name:
                        plt.figure(figsize=(12, 8))
                        plt.title("Boxplot between {} and {}.".format(i, target_column_name))
                        sns.boxplot(x=i, y=target_column_name, data=data)
                        plt.show()
                print()            
            else:
                print("There are no categorical data present in the given data.")
                print()
        elif regression == False and type(target_column_name) == str and (target_column_name in discrete_data or target_column_name in categorical_data):
            print('*' * round(data.shape[1] / 2) + " "+"Bivariate Analysis on numerical data" + " "+'*' * round(data.shape[1] / 2))
            if len(numerical_data) > 0:
                for i in numerical_data:
                    if i != target_column_name:
                        plt.figure(figsize=(12, 8))
                        plt.title("Boxplot between {} and {}.".format(i, target_column_name))
                        sns.boxplot(x=target_column_name, y=i, data=data)
                        plt.show()
                print()            
            else:
                print("There are no numerical data present in the given data.")
                print()
                
            print('*' * round(data.shape[1] / 2) + " "+"Bivariate Analysis on discrete data" + " "+'*' * round(data.shape[1] / 2))
            if len(discrete_data) > 0:
                for i in discrete_data:
                    if i != target_column_name:
                        print("Cross tabulation between {} and {}.".format(i, target_column_name))
                        display(pd.crosstab(data[i], data[target_column_name]))
                        print()
                print()            
            else:
                print("There are no discrete data present in the given data.")
                print()
                
            print('*' * round(data.shape[1] / 2) + " "+"Bivariate Analysis on categorical data" + " "+'*' * round(data.shape[1] / 2))
            if len(categorical_data) > 0:
                for i in categorical_data:
                    if i != target_column_name:
                        print("Cross tabulation between {} and {}.".format(i, target_column_name))
                        display(pd.crosstab(data[i], data[target_column_name]))
                        print()
                print()            
            else:
                print("There are no categorical data present in the given data.")
                print()
        else:
            print("There may be an wrong input given in target_column_name or regression parameter. Please check and try again.")
            print()
    else:
        
        print("The given data is not a dataframe.")


# In[3]:


def train_data_handling(data, file_to_dump, regression, target_column_name, min_outlier_fill = 0.10, max_outlier_fill = 0.90):
    
    """The function train_data_handling() is used to handle null values and outliers in the dataset.
       This function is only used for training dataset. Don't use it for test dataset.
       It seperates the given data into numerical data, discrete data and categorical data.
       
       For numerical data, the null values are filled based on the skewness of the data.
       For discrete and categorical data the null values are filled randomly based on their unique values.
       
       The outliers in numerical data are cured by quantile or percentile method by passing the value between 0.10 to 0.90.
       
       train_data_handling(data, file_to_dump, regression, target_column_name, min_outlier_fill, max_outlier_fill)
       This function contains six arguments.
           
           data -> We need to pass the entire train dataframe. (type = dataframe)
           file_to_dump -> We need to pass the file name to dump the handling_na_values and handling_outliers values for 
                           future use. (type = str)
           regression -> We need to pass the supervised learning type based on the target_column_name. (type = bool)
                   True -> target_column is numerical.
                   False -> target_column is discrete or categorical.
           target_colum_name -> We need to pass the column name of the target variable (y). (type = string)
           min_outlier_fill -> We need to pass the quantile value to replace the minimum outlier. (type = float or int)
                               range = 0.10 to 0.50
           max_outlier_fill -> We need to pass the quantile value to replace the maximum outlier. (type = float or int)
                               range = 0.50 to 0.90
                               
            This function will return a dataframe which has no null values and outliers.
            
            Example: train_data_handling(data = dataframe, file_to_dump = "file name", regression = True, target_column_name = column_name)
                     train_data_handling(data = dataframe, file_to_dump = "file name", regression = False, target_column_name = column_name,
                     min_outlier_fill = 0.45, max_outlier_fill = 0.85)"""
    
    import pandas as pd
    import numpy as np
    import random
    from joblib import load, dump
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame:
        
        if type(file_to_dump) == str:
            
            data_numerical = list(data.select_dtypes(exclude=['object', 'category', 'datetime64']).columns)
            numerical_data = []
            discrete_data = []
            categorical_data = list(data.select_dtypes(include=['object', 'category']).columns)
        
            for i in data_numerical:
                if data[i].nunique() > 20:
                    numerical_data.append(i)
        
            for i in data_numerical:
                if i not in numerical_data:
                    discrete_data.append(i)
                    
            if len(categorical_data) > 0:
                
                for i in categorical_data:
                    find_unique = list(data[i].unique())
                    if np.nan in find_unique:

                        find_unique.remove(np.nan)
                    data[i].fillna(data[i].apply(lambda x : random.choice(find_unique) if x is np.nan else x), inplace=True)

                print('*' * round(data.shape[1] / 2) + " "+"Filling null values in the data" + " "+'*' * round(data.shape[1] / 2))
                print()
                print('*' * round(data.shape[1] / 2) + " "+"Filling null values in categorical data" + " "+'*' * round(data.shape[1] / 2))
                display(data[categorical_data].isna().sum())
                print()
            else:
                
                print("There are no categorical data present in the dataset.")
                print()
                
            if len(discrete_data) > 0:
                
                for i in discrete_data:
                    find_unique = list(data[i].unique())
                    if np.nan in find_unique:

                        find_unique.remove(np.nan)
                    data[i].fillna(data[i].apply(lambda x : random.choice(find_unique) if x is np.nan else x), inplace=True)

                print('*' * round(data.shape[1] / 2) + " "+"Filling null values in discrete data" + " "+'*' * round(data.shape[1] / 2))
                print()
                display(data[discrete_data].isna().sum())
                print()
            
            else:
                
                print("There are no discrete data present in the dataset.")
                print()
                
            if len(numerical_data) > 0:
                
                handling_numerical_na = dict()
                for i in numerical_data:
                    numerical_data_skew = data[i].skew()
                    if numerical_data_skew >= -1 and numerical_data_skew <= 1:
                        
                        numerical_data_fill = round(data[i].mean())
                        
                    else:
                        
                        numerical_data_fill = round(data[i].median())
                    
                    handling_numerical_na[i] = numerical_data_fill
                    
                for i in numerical_data:
                    data[i].fillna(handling_numerical_na[i], inplace=True)
                    
                print('*' * round(data.shape[1] / 2) + " "+"Filling null values in numerical data" + " "+'*' * round(data.shape[1] / 2))
                print()
                display(data[numerical_data].isna().sum())
                print()
                
                handling_na_name = "Numerical_na_handling_"+file_to_dump
                dump(handling_numerical_na, handling_na_name)
                print("For future use, numerical null value handling are stored in a dictionary object as {}.".format(handling_na_name))
            
            else:
                
                print("There are no numerical data present in the dataset.")
            
            print('*' * round(data.shape[1] / 2) + " "+"Find and cure outliers in numerical data" + " "+'*' * round(data.shape[1] / 2))
            print()
            
            if regression == True and type(target_column_name) == str and target_column_name in numerical_data:
                
                numerical_data_copy = numerical_data.copy()
                numerical_data_copy.remove(target_column_name)
                
                if len(numerical_data_copy) > 0:
                
                    if (min_outlier_fill >=0.10 and min_outlier_fill <= 0.50) and (max_outlier_fill >= 0.50 and max_outlier_fill <= 0.90):
                    
                        handling_outliers = dict()
                        for i in numerical_data_copy:
                            q1 = np.nanquantile(data[i], 0.25)
                            q3 = np.nanquantile(data[i], 0.75)
                            iqr = q3- q1
                            lower_bound = round(q1 - (1.5 * iqr))
                            upper_bound = round(q3 + (1.5 * iqr))
                            handling_outliers[i] = list()
                            handling_outliers[i].append(lower_bound)
                            handling_outliers[i].append(upper_bound)
                        
                        for i in numerical_data_copy:
                            data[i] = data[i].map(lambda x: np.nanquantile(data[i], min_outlier_fill) if x < handling_outliers[i][0] else x)
                            data[i] = data[i].map(lambda x: np.nanquantile(data[i], max_outlier_fill) if x > handling_outliers[i][1] else x)
                    
                        handling_outlier_name = "Numerical_outliers_handling_"+file_to_dump
                        dump(handling_outliers, handling_outlier_name)
                        print("For future use, numerical outlier handling values are stored in a dictionary object as {}.".format(handling_outlier_name))
          
                    else:
                        
                        print("Please check the range values provided for outliers")
            
                else:
                
                    print("There are no numerical data present in the dataset to treat outliers.")
                
            elif regression == False and type(target_column_name) == str:
                
                numerical_data_copy = numerical_data.copy()
                
                if len(numerical_data_copy) > 0:
                
                    if (min_outlier_fill >=0.10 and min_outlier_fill <= 0.50) and (max_outlier_fill >= 0.50 and max_outlier_fill <= 0.90):
                    
                        handling_outliers = dict()
                        for i in numerical_data_copy:
                            q1 = np.nanquantile(data[i], 0.25)
                            q3 = np.nanquantile(data[i], 0.75)
                            iqr = q3- q1
                            lower_bound = round(q1 - (1.5 * iqr))
                            upper_bound = round(q3 + (1.5 * iqr))
                            handling_outliers[i] = list()
                            handling_outliers[i].append(lower_bound)
                            handling_outliers[i].append(upper_bound)
                        
                        for i in numerical_data_copy:
                            data[i] = data[i].map(lambda x: np.nanquantile(data[i], min_outlier_fill) if x < handling_outliers[i][0] else x)
                            data[i] = data[i].map(lambda x: np.nanquantile(data[i], max_outlier_fill) if x > handling_outliers[i][1] else x)
                    
                        handling_outlier_name = "Numerical_outliers_handling_"+file_to_dump
                        dump(handling_outliers, handling_outlier_name)
                        print("For future use, numerical outlier handling values are stored in a dictionary object as {}.".format(handling_outlier_name))
          
                    else:
                        
                        print("Please check the range values provided for outliers")
            
                else:
                
                    print("There are no numerical data present in the dataset to treat outliers.")
                
            else:
                
                print("There is an error in the given input. Please check and try again.")
            
            return data
        
        else:
            
            print("Please give a valid file name.")
    
    else:
        
        print("The given data is not a dataframe.")


# In[4]:


def test_data_handling(data, na_file: str, outlier_file: str, regression: bool, min_outlier_fill = 0.10, max_outlier_fill = 0.90):
    
    """The function test_data_handling() is used to handle the null values and outliers
       on the test data based on the file created by the function train_data_handling().
       
       test_data_handling(data, na_file: str, outlier_file: str, regression: bool, min_outlier_fill = 0.10, max_outlier_fill = 0.90)
           This function contains six arguments.
           
           data -> We need to pass the entire train dataframe. (type = dataframe)
           na_file -> We need to pass the file name to load the handling_na_values to fill null values in test data. (type = str)
           outlier_file -> We need to pass the file name to load the handling_outliers values to replace outliers in test data. (type = str)
           regression -> We need to pass the supervised learning type based on the target_column_name. (type = bool)
                   True -> target_column is numerical.
                   False -> target_column is discrete or categorical.
           min_outlier_fill -> We need to pass the quantile value to replace the minimum outlier. (type = float or int)
                               range = 0.10 to 0.50
           max_outlier_fill -> We need to pass the quantile value to replace the maximum outlier. (type = float or int)
                               range = 0.50 to 0.90
                               
            This function will return a dataframe which has no null values and outliers.
            
            Example: train_data_handling(data = dataframe, na_file = "file name", outlier_file = "file name", regression = True)
                     train_data_handling(data = dataframe, na_file = "file name", outlier_file = "file name", regression = False, target_column_name = column_name,
                     min_outlier_fill = 0.45, max_outlier_fill = 0.85)"""
    
    import pandas as pd
    import numpy as np
    import os
    import random
    from joblib import load, dump
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame:
        
        current_path = os.getcwd()
        na_path = current_path+"//"+na_file
        outlier_path = current_path+"//"+outlier_file
        
        if os.path.exists(na_path) and os.path.exists(outlier_path):
            
            data_numerical = list(data.select_dtypes(exclude=['object', 'category', 'datetime64']).columns)
            numerical_data = []
            discrete_data = []
            categorical_data = list(data.select_dtypes(include=['object', 'category']).columns)
        
            for i in data_numerical:
                if data[i].nunique() > 20:
                    numerical_data.append(i)
        
            for i in data_numerical:
                if i not in numerical_data:
                    discrete_data.append(i)
                    
            print('*' * round(data.shape[1] / 2) + " "+"Filling null values in test data" + " "+'*' * round(data.shape[1] / 2))
            print()
            if len(categorical_data) > 0:
                
                for i in categorical_data:
                    find_unique = list(data[i].unique())
                    if np.nan in find_unique:
                        
                        find_unique.remove(np.nan)
                    data[i].fillna(data[i].apply(lambda x : random.choice(find_unique) if x is np.nan else x), inplace=True)
                print('*' * round(data.shape[1] / 2) + " "+"Null values in categorical data are replaced in test data" + " "+'*' * round(data.shape[1] / 2))
                print()
                
            if len(discrete_data) > 0:
                
                for i in discrete_data:
                    find_unique = list(data[i].unique())
                    if np.nan in find_unique:
                        
                        find_unique.remove(np.nan)
                    data[i].fillna(data[i].apply(lambda x : random.choice(find_unique) if x is np.nan else x), inplace=True)
                print('*' * round(data.shape[1] / 2) + " "+"Null values in discrete data are replaced in test data" + " "+'*' * round(data.shape[1] / 2))
                print()
                
            if len(numerical_data) > 0:
                
                handling_na = load(na_file)
                if type(handling_na) == dict:
                    
                    if regression == True:
                        
                        if len(handling_na) - 1 == len(numerical_data):
                            
                            for i in numerical_data:
                                data[i].fillna(handling_na[i], inplace=True)
                            print('*' * round(data.shape[1] / 2) + " "+"Null values in numerical data are replaced in test data" + " "+'*' * round(data.shape[1] / 2))
                            print()
                        
                        else:
                            
                            print("There is a mismatch in the given file and numerica data. Please check and try.")
                            
                    elif regression == False:
                        
                        if len(handling_na) == len(numerical_data):
                            
                            for i in numerical_data:
                                data[i].fillna(handling_na[i], inplace=True)
                            print('*' * round(data.shape[1] / 2) + " "+"Null values in numerical data are replaced in test data" + " "+'*' * round(data.shape[1] / 2))
                            print()
                        
                        else:
                            
                            print("There is a mismatch in the given file and numerica data. Please check and try.")
                    
                    else:
                        
                        print("Regression parameter takes boolean inputs, so check and try again.")
                
                else:
                    
                    print("This is a wrong file. Because it doesn't match the provided data type dictionary.")
            
            print('*' * round(data.shape[1] / 2) + " "+"Replacing outliers in numerical data in test data" + " "+'*' * round(data.shape[1] / 2))
            print()
            
            if len(numerical_data) > 0:
                
                handling_outlier = load(outlier_file)
                if type(handling_outlier) == dict:
                    
                    if len(handling_outlier) == len(numerical_data):
                        
                        for i in numerical_data:
                            data[i] = data[i].map(lambda x: np.nanquantile(data[i], min_outlier_fill) if x < handling_outlier[i][0] else x)
                            data[i] = data[i].map(lambda x: np.nanquantile(data[i], max_outlier_fill) if x > handling_outlier[i][1] else x)
                        print('*' * round(data.shape[1] / 2) + " "+"Outliers in numerical data are replaced in test data" + " "+'*' * round(data.shape[1] / 2))
                        print()
                              
                    else:
                       
                        print("There is a mismatch in the given file and numerica data. Please check and try.")
                
                else:
                    
                    print("This is a wrong file. Because it doesn't match the provided data type dictionary.")
        
        else:
            
            print("There is an error in file name given. Either file should be present in current directory or given file name is wrong.")
            
        return data
    
    else:
        
        print("The given data is not a dataframe.")


# In[5]:


def data_corr(data, target_column_name: str, corr_file_name: str):
    
    """The function data_corr() is used to get the correlation and p_value
       using spearman method.Because it can see both linear and non-linear data correlation.
       This function will neglect datetime columns present in the given data.
       It produce a dataframe for correlation and p_value and stored in the given file name
       
       data_corr(data, target_column_name, corr_file_name) contains three arguments.
           
           data -> We need to pass entire train dataframe. (type = dataframe)
           target_column_name -> We need to provide the column name of the target variable (y). (type = str)
           corr_file_name -> We need to pass a name to save the generated correlation dataframe. (type = str)
           
           This function will return a dataframe which does not contain any datetime column in the given dataframe.
           
           Example: data_corr(data = dataframe, target_column_name = "column_name", corr_file_name = "file_name")"""
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.stats as ss
    from joblib import load, dump
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame:
        
        data_column = list(data.columns)
        date_data = list(data.select_dtypes(include=['datetime64']).columns)
        categorical_data = list(data.select_dtypes(include=['object', 'category']).columns)
        
        if len(date_data) > 0:
            
            for i in date_data:
                data_column.remove(i)
        
        if data[data_column].isna().sum().sum() == 0:
            
            if type(target_column_name) == str and target_column_name in data_column:
                
                correlation = []
                p_value = []
                column_name = []
                data_type = []
                
                for i in data_column:
                    if i != target_column_name:
                        
                        corr, p_val = ss.spearmanr(data[i], data[target_column_name])
                        correlation.append(corr)
                        p_value.append(p_val)
                        column_name.append(i)
                        
                        if i in categorical_data:
                            
                            data_type.append("categorical")
                            
                        else:
                            
                            data_type.append("numerical")
                        
                correlation_data = {"column_name" : column_name,
                                    "correlation_value" : correlation,
                                    "p_value" : p_value,
                                    "data_type" : data_type}
                
                correlation_dataframe = pd.DataFrame(correlation_data)
                
                print('*' * round(data.shape[1] / 2) + " "+"Correlation and p_value for the given data" + " "+'*' * round(data.shape[1] / 2))
                print()
                display(correlation_dataframe)
                
                if type(corr_file_name) == str:
                    
                    correlation_name = "correlation_"+corr_file_name
                    dump(correlation_dataframe, correlation_name)
                    print("Correlation dataframe is stored as {} file and can used for future purpose.".format(correlation_name))
                    
                else:
                    
                    print("The provided input yo corr_file_name is incorrect data type. It needs to be string.")
                
                return data[data_column]
            
            else:
                
                print("Either the argument passed to target_column_name is string or the given target_column_name is not present in the given dataset.")
        
        else:
            
            print("There is null values present in the data, so please handle the values and try again.")
    
    else:
        
        print("The given data is not a dataframe.")


# In[6]:


def data_encode_and_scale(data, test_data, target_column_name: str, correlation_file_name: str, confidence_level: int, file_name: str):
    
    """The function data_encode_and_scale() is used to encode the categorical data 
       and scale the dataframe using standard scaler.
       
       If the test data is given in a dataframe this fuction will return two dataframe.
       
       data_encode_and_scale(data, test_data, target_column_name: str, correlation_file_name: str, confidence_level: int, file_name: str)
                             contains six arguments.
                             
                data -> We need to pass the entire dataframe. (type = dataframe)
                test_data -> We need to pass the test dataframe if available or any python object. (type = dataframe)
                target_column_name -> We need to provide the column name of the target variable (y). (type = str)
                correlation_file_name -> We need to pass the file that is generated by the function train_data_handling(). (type = str)
                confidence_level -> We need to pass an integer between 0 to 100 to get the p_value to select the features from dataframe. (type = int)
                file_name -> We need to pass a file name to save the encoding and scaling method to use in future.
                
        Example : data_encode_and_scale(data = "dataframe", test_data = "dataframe", target_column_name = "column_name", correlation_file_name: "correlation_file", confidence_level = 94, file_name = "file_name")
                    It will return a two dataframe which are scaled train dataframe and scaled test dataframe"""
    
    import pandas as pd
    import numpy as np
    import scipy.stats as ss
    import os
    from joblib import load, dump
    from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, LabelEncoder
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame and data.isna().sum().sum() == 0:
        
        current_directory = os.getcwd()
        correlation_path = current_directory+"//"+correlation_file_name
        
        if type(correlation_file_name) == str and os.path.exists(correlation_path):
            
            correlation_data = load(correlation_file_name)
            categorical_data = list(data.select_dtypes(include=['object', 'category']).columns)
            data_column = list(data.columns)
            
            if type(target_column_name) == str and target_column_name in data_column:
                
                if type(confidence_level) == int and confidence_level in list(range(0, 101)):
                    
                    given_p_value = 1 - (confidence_level / 100)
                    p_value_dataframe = correlation_data[correlation_data['p_value'] <= given_p_value]
                    print("*" * round(data.shape[1] / 2) +" "+"Selected column based on confidence interval"+" "+"*" * round(data.shape[1] / 2))
                    print()
                    display(p_value_dataframe)
                    numerical_p_value = p_value_dataframe[p_value_dataframe['data_type'] == "numerical"]
                    numerical_p_value_column = list(numerical_p_value['column_name'])
                    
                    if p_value_dataframe.shape[0] > 0:
                        
                        categorical_p_value = p_value_dataframe[p_value_dataframe['data_type'] == "categorical"]
                        
                        if categorical_p_value.shape[0] > 0:
                            
                            categorical_p_value_column = list(categorical_p_value['column_name'])
                            low_unique_column = []
                            high_unique_column = []
                            for i in categorical_p_value_column:
                                if data[i].nunique() <= 5:
                                    low_unique_column.append(i)
                                else:
                                    high_unique_column.append(i)
                            if len(low_unique_column) > 0:
                                ordinal_encode = OrdinalEncoder()
                                ordinal_encode.fit(data[low_unique_column])
                                ordinal_encode_data = ordinal_encode.transform(data[low_unique_column])
                                ordinal_encode_dataframe = pd.DataFrame(ordinal_encode_data, columns=low_unique_column)
                                dump(ordinal_encode, "ordinal_encoding_"+str(file_name))
                                print("Ordinal encoding file is saved as ordinal_encoding_{}.".format(str(file_name)))
                                print()
                            else:
                                ordinal_encode_dataframe = pd.DataFrame()
                                
                            if len(high_unique_column) > 0:
                                one_hot_encode = OneHotEncoder()
                                one_hot_encode.fit(data[high_unique_column])
                                one_hot_encode_data = one_hot_encode.transform(data[high_unique_column]).toarray()
                                one_hot_column = list(one_hot_encode.get_feature_names_out())
                                one_hot_encode_dataframe = pd.DataFrame(one_hot_encode_data, columns=one_hot_column)
                                dump(one_hot_encode, "one_hot_encoding_"+str(file_name))
                                print("One hot encoding file is saved as one_hot_encoding_{}.".format(str(file_name)))
                                print()
                            else:
                                one_hot_encode_dataframe = pd.DataFrame()
                            
                            if target_column_name in categorical_data and target_column_name not in categorical_p_value_column:
                                label_encode = LabelEncoder()
                                label_encode.fit(data[target_column_name])
                                label_encode_data = label_encode.transform(data[target_column_name])
                                lable_encode_dataframe = pd.DataFrame(label_encode_data, columns=[target_column_name])
                                dump(label_encode, "lable_encoding"+str(file_name))
                                print("Lable encoding file is saved as lable_encoding_{}.".format(str(file_name)))
                                print()
                            else:
                                lable_encode_dataframe = pd.DataFrame(np.array(data[target_column_name]), columns=[target_column_name])
                                
                            if len(numerical_p_value_column) > 0:
                                numerical_dataframe = data[numerical_p_value_column]
                            else:
                                numerical_dataframe = pd.DataFrame()
                                
                            dataframe = numerical_dataframe.join(ordinal_encode_dataframe)
                            dataframe = dataframe.join(one_hot_encode_dataframe)
                            
                            print("*" * round(data.shape[1] / 2) +" "+"Encoded dataframe"+" "+"*" * round(data.shape[1] / 2))
                            print()
                            display(dataframe.head())
                            
                            scale = StandardScaler()
                            scale.fit(dataframe)
                            scale_column = list(scale.get_feature_names_out())
                            scaled_data = scale.transform(dataframe)
                            scaled_dataframe = pd.DataFrame(scaled_data, columns=scale_column)
                            
                            print("*" * round(data.shape[1] / 2) +" "+"Scaled dataframe"+" "+"*" * round(data.shape[1] / 2))
                            print()
                            scaled_dataframe = scaled_dataframe.join(lable_encode_dataframe)
                            display(scaled_dataframe.head())
                            
                            if type(test_data) == pd.core.frame.DataFrame and (len(data.columns) - 1 == len(test_data.columns)) and (test_data.isna().sum().sum() == 0):
                                if len(low_unique_column) > 0:
                                    ordinal_encode_test_dataframe = pd.DataFrame(ordinal_encode.transform(test_data[low_unique_column]), columns=low_unique_column)
                                else:
                                    ordinal_encode_test_dataframe = pd.DataFrame()
                                if len(high_unique_column) > 0:
                                    one_hot_encode_test_dataframe = pd.DataFrame(one_hot_encode.transform(test_data[high_unique_column]).toarray(), columns=one_hot_column)
                                else:
                                    one_hot_encode_test_dataframe = pd.DataFrame()
                                if len(numerical_p_value_column) >0:
                                    numerical_test_dataframe = test_data[numerical_p_value_column]
                                else:
                                    numerical_test_dataframe = pd.DataFrame()
                                    
                                test_dataframe = numerical_test_dataframe.join(ordinal_encode_test_dataframe)
                                test_dataframe = test_dataframe.join(one_hot_encode_test_dataframe)
                                
                                print("*" * round(data.shape[1] / 2) +" "+"Encoded test dataframe"+" "+"*" * round(data.shape[1] / 2))
                                print()
                                display(test_dataframe.head())
                                
                                print("*" * round(data.shape[1] / 2) +" "+"Scaled test dataframe"+" "+"*" * round(data.shape[1] / 2))
                                print()
                                scaled_test_dataframe = pd.DataFrame(scale.transform(test_dataframe), columns=scale_column)
                                display(scaled_test_dataframe.head())
                                
                                return scaled_dataframe, scaled_test_dataframe
                                
                            else:
                                print("The test data is not a dataframe or the columns provided doesn't match or the test data contains null values.")
                                scaled_test_dataframe = pd.DataFrame()
                                return scaled_dataframe, scaled_test_dataframe
                        
                        else:
                            print("There are no categorical column present for the given confidence level.")
                            scale = StandardScaler()
                            scale.fit(data[numerical_p_value_column])
                            scale_column = list(scale.get_feature_names_out())
                            scaled_data = scale.transform(data[numerical_p_value_column])
                            scaled_dataframe = pd.DataFrame(scaled_data, columns=scale_column)
                            
                            print("*" * round(data.shape[1] / 2) +" "+"Scaled dataframe"+" "+"*" * round(data.shape[1] / 2))
                            print()
                            lable_encode_dataframe = pd.DataFrame(np.array(data[target_column_name]), columns=[target_column_name])
                            scaled_dataframe = scaled_dataframe.join(lable_encode_dataframe)
                            display(scaled_dataframe.head())
                            scaled_test_dataframe = pd.DataFrame()
                            
                            if type(test_data) == pd.core.frame.DataFrame and (len(data.columns) - 1 == len(test_data.columns)) and (test_data.isna().sum().sum() == 0):
                                print("*" * round(data.shape[1] / 2) +" "+"Scaled test dataframe"+" "+"*" * round(data.shape[1] / 2))
                                print()
                                scaled_test_dataframe = pd.DataFrame(scale.transform(data[numerical_p_value_column]), columns=scale_column)
                                display(scaled_test_dataframe.head())
                                return scaled_dataframe, scaled_test_dataframe
                            else:
                                scaled_test_dataframe = pd.DataFrame() 
                                return scaled_dataframe, scaled_test_dataframe
                    
                    else:
                        
                        print("Please change the confidence level, because no column has the p_value for the given confidence level.")
                
                else:
                   
                    print("Either the given confidence level is not an integer datatype or the given confidence level is not inbetween 0 to 100.")
            
            else:
                
                print("Either the given target column name is not an string datatype or the given target column is not present in the given data.")
            
        else:
            
            print("Either the given file name is not a string datatype or the given file is not present in the current working directory.")
            
    else:
        
        print("The given data is not a dataframe or it contains null values.")


# In[7]:


def train_model(data, file_name: str, target_column_name: str, regression: bool):
    
    """The function train_model() is used to train the machine learning model
       for the given data.
       
       train_model(data, file_name: str, target_column_name: str, regression: bool) contains four arguments
       
           data -> We need to provide entire dataframe. (type = dataframe)
           file_name -> We need to provide the file name to save the model for future use. (type = str)
           target_column_name -> We need to provide the name of the target column name. (type = str)
           regression -> We need to provide a boolean data type whether the ml model is regression or classification. (type = bool)
           
           The function train_model() will return a dataframe that contains the information about the trained model.
           
               Example: train_model(data = dataframe, file_name = "file_name", target_column_name = "column_name", regression = True)
                        train_model(data = dataframe, file_name = "file_name", target_column_name = "column_name", regression = False)"""
    
    import pandas as pd
    import numpy as np
    import os
    from sklearn.metrics import f1_score, mean_absolute_error, mean_squared_error, precision_score, accuracy_score
    from sklearn.linear_model import LinearRegression, LogisticRegression, Lasso, Ridge, RidgeClassifier
    from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingRegressor, GradientBoostingClassifier, AdaBoostRegressor, AdaBoostClassifier, BaggingRegressor, BaggingClassifier
    from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier, ExtraTreeRegressor, ExtraTreeClassifier
    from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
    from sklearn.svm import SVC 
    from joblib import load, dump
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame:
        if data.isna().sum().sum() == 0:
            if target_column_name in list(data.columns):
                data_column = list(data.columns)
                data_column.remove(target_column_name)
                X = data[data_column]
                y = data[target_column_name]
                if regression == True:
                    mae_list = []
                    rmse_list = []
                    algo = []
                    score = []
                    adjusted_r2_score = []
                    
                    model = LinearRegression()
                    model.fit(X, y)
                    pred = model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Linear Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Linear_regression_"+str(file_name))
                    
                    model = Lasso()
                    model.fit(X, y)
                    pred = model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Lasso Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Lasso_regression_"+str(file_name))
                    
                    model = Ridge()
                    model.fit(X, y)
                    pred = model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Ridge Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Ridge_regression_"+str(file_name))
                    
                    model = RandomForestRegressor()
                    model.fit(X, y)
                    pred= model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Random Forest Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Random_forest_regression_"+str(file_name))
                    
                    model = KNeighborsRegressor()
                    model.fit(X, y)
                    pred= model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("KNN Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Knn_regression_"+str(file_name))
                    
                    model = DecisionTreeRegressor()
                    model.fit(X, y)
                    pred= model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Decision Tree Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Decision_tree_regression_"+str(file_name))
                    
                    model = GradientBoostingRegressor()
                    model.fit(X, y)
                    pred= model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Gradient Bosting Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Gradient_boosting_regression_"+str(file_name))
                    
                    model = AdaBoostRegressor()
                    model.fit(X, y)
                    pred= model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Ada Boost Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Ada_boost_regression_"+str(file_name))
                    
                    model = BaggingRegressor()
                    model.fit(X, y)
                    pred= model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Bagging Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Bagging_regression_"+str(file_name))
                    
                    model = ExtraTreeRegressor()
                    model.fit(X, y)
                    pred= model.predict(X)
                    mae = mean_absolute_error(y_true=y, y_pred=pred)
                    mse = np.sqrt(mean_squared_error(y_true=y, y_pred=pred))
                    algo.append("Extra tree Regression")
                    mae_list.append(mae)
                    rmse_list.append(mse)
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    dump(model, "Extra_tree_regression_"+str(file_name))
                    
                    dataframe = pd.DataFrame({"Algorithm_name" : algo,
                                             "Mean_absolute_error" : mae_list,
                                             "Root_mean_squared_error" : rmse_list,
                                              "Adjusted_r2_score" : adjusted_r2_score,
                                             "Model_score" : score})
                    
                    return dataframe
                    
                elif regression == False:
                    accuracy_list = []
                    f1_score_list = []
                    precision_score_list = []
                    adjusted_r2_score = []
                    algo = []
                    score = []
                    
                    model = LogisticRegression()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Logistic_regression")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Logistic_regression_"+str(file_name))
                    
                    model = RidgeClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Ridge_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Ridge_classifier_"+str(file_name))
                    
                    model = KNeighborsClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Knn_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Knn_classifier_"+str(file_name))
                    
                    model = RandomForestClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Random_forest_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Random_forest_classifier_"+str(file_name))
                    
                    model = SVC()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("SVC_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "SVC_classifier_"+str(file_name))
                    
                    model = DecisionTreeClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Decision_tree_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Decision_tree_classifier_"+str(file_name))
                    
                    model = GradientBoostingClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Gradient_boosting_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Gradient_boosting_classifier_"+str(file_name))
                    
                    model = AdaBoostClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Ada_boost_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Ada_boost_classifier_"+str(file_name))
                    
                    model = BaggingClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Bagging_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Bagging_classifier_"+str(file_name))
                    
                    model = ExtraTreeClassifier()
                    model.fit(X, y)
                    pred = model.predict(X)
                    accuracy_list.append(accuracy_score(y_true = y, y_pred = pred))
                    algo.append("Extra_tree_classifier")
                    score.append(model.score(X, y))
                    adjusted_r2_score.append(1 - ( 1-model.score(X, y) ) * ( len(y) - 1 ) / ( len(y) - X.shape[1] - 1 ))
                    f1_score_list.append(f1_score(y_true = y, y_pred = pred))
                    precision_score_list.append(precision_score(y_true = y, y_pred = pred))
                    dump(model, "Extra_tree_classifier_"+str(file_name))
                    
                    dataframe = pd.DataFrame({"Algorithm_name" : algo,
                                              "Model_precision" : precision_score_list,
                                              "Model_f1_score" : f1_score_list,
                                              "Adjusted_r2_score" : adjusted_r2_score,
                                              "Model_accuracy_score" : accuracy_list,
                                              "Model_score" : score})
                    return dataframe
                    
                else:
                    print("The value passed to the parameter regression needs to be boolean data type.")
            else:
                print("The given target column is not present in the given data.")
        else:
            print("The given data consist of null values.")
    else:
        print("The given data is not a dataframe.")


# In[8]:


def test_model(data, test_data, train_file_name: str, target_column_name: str):
    
    """The function test_model() is used to predict the target variable for the test data.
    
       test_model(data, test_data, train_file_name: str, target_column_name: str) contains four arguments
       
           data -> We need to provide the entire dataframe on which the train_model() is built. (type = dataframe)
           test_data -> We need to provide the test dataframe to predict the target variable. (type = dataframe)
           train_file_name -> We need to provide the any one train file name which is generated by train_model() function. (type = str)
           target_column_name -> We need to provide the target column name of the given data. (type = str)
           
           The function test_model() will return an array of predicted value for the given test data.
           
               Example: test_model(data = dataframe, test_model = test_dataframe, train_file_name = "file_name", target_column_name = "column_name")"""
    
    import pandas as pd
    import numpy as np
    import os 
    from joblib import load, dump
    import warnings
    warnings.filterwarnings('ignore')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option('display.float_format', '{:.6f}'.format)
    
    if type(data) == pd.core.frame.DataFrame and type(test_data) == pd.core.frame.DataFrame:
        if target_column_name not in list(test_data.columns):
            if len(data.columns) - 1 == len(test_data.columns):
                train_data_column = list(data.columns)
                train_data_column.remove(target_column_name)
                test_data_column = list(test_data.columns)
                if train_data_column == test_data_column:
                    current_directory = os.getcwd()
                    path = current_directory+"//"+train_file_name
                    if os.path.exists(path):
                        model = load(train_file_name)
                        pred = model.predict(test_data)
                        score = model.score(test_data, pred)
                        print("The model score for the test data and predicted value is {}.".format(score))
                        return pred
                    else:
                        print("The train file name is not present in the current directory")
                else:
                    print("Column in data and test data is different.")
            else:
                print("There is a mismatch in the column in data and test data.")
        else:
            print("The given target column name is present in the test data. Please remove the column and try again.")
    else:
        print("Either the data is not a dataframe or the test data is not a dataframe.")


# In[ ]:




