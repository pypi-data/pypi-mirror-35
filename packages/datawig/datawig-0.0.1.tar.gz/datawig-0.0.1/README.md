DataWig - Imputation for Tables
================================

DataWig learns models to impute missing values in tables. 

For each to-be-imputed column, DataWig trains a supervised machine learning model
to predict the observed values in that column from the values in other columns  


# Installation

The easiest way to install the package is to use virtualenvs and pip.

Set up virtualenv in the root dir of the package:

```
python3.6 -m venv venv
```

Install the package 

```
./venv/bin/pip install -e .
```

Run tests:

```
./venv/bin/pip install -r requirements/requirements.dev.txt
./venv/bin/python -m pytest

```

# Usage 

The imputation API is expecting your data as a [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).
 
For most use cases, the `SimpleImputer` class is the best starting point.
DataWig expects you to provide the column name of the column you would like to impute values for (called `output_column` below) and some column names 
that contain values that you deem useful for imputing the values in the to-be-imputed column (called `input_columns` below). 


 ```python
    from datawig import SimpleImputer
    import pandas as pd
    
    # some test data stored in the test/resources folder
    
    df_train = pd.read_csv("training_data.csv")
    df_test = pd.read_csv("testing_data_files.csv")

    # this is where the model artifacts and metrics will be stored
    output_path = "imputer_model"

    # Initialize and train Imputer
    imputer = SimpleImputer(
        input_columns=["item_name", "bullet_point"], # columns containing information about the column we want to impute
        output_column="brand" # the column we'd like to impute values for
        ).fit(train_df=df_train)
    
    # Impute missing values on test data
    imputed = imputer.predict(df_test)

 ```
