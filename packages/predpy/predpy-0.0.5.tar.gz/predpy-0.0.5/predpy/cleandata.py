import operator
import numpy as np
import pandas as pd
import stringcase


def rename_columns(df):
    """ all column labels in lower_snake_case
        INPUT:
            df:
                A dataframe.
        OUTPUT:
            df:
                The same dataframe, with renamed columns.
    """
    replacers = {}
    for name in df.columns:
        replacers[name] = stringcase.snakecase(name.lower()).replace('__', '_')
    df = df.rename(index=int, columns=replacers)
    return df


def add_feature_continuous_condition(df_X, cont_feature_name, indicator, number):
    """ Add a feature to the dataframe where a continuous feature matches a conditional.
        (Ex: 'acorns < 0'), replacing them with the mean. This removes the continuous variables' effects in this region.
        INPUT:
            df_X:
                A dataframe of independent variables.
            cont_feature_name:
                string, the continuous varible to set condition
            indicator:
                string, a conditional (like "<" or '==')
            number:
                a float or int, compares to conditional
        OUTPUT:
            df_X:
                The same dataframe, with meaned values that fit the condition and a new feature (of 0's and 1's).
    """
    ops = {"==": operator.is_,
           "!=": operator.is_not,
           '<': operator.lt,
           '<=': operator.le,
           '>': operator.gt,
           '>=': operator.ge}
    nulls = pd.isnull(df_X[cont_feature_name])
    if nulls.any():
        df_X[cont_feature_name + "_is_null"] = nulls
        df_X.loc[nulls, cont_feature_name
                 ] = np.mean(df_X.loc[~nulls, cont_feature_name])
#     df_X[cont_feature_name + "_is_na"] = pd.isna(df_X[cont_feature_name])
#     df_X[cont_feature_name][~pd.isna(df_X[cont_feature_name])] = np.mean(df_X[cont_feature_name][~pd.isna(df_X[cont_feature_name])])
    df_X[cont_feature_name + "_" + str(indicator) + "_" + str(
        number)] = ops[indicator](df_X[cont_feature_name], number)
    # df_X[cont_feature_name][ops[indicator](df_X[cont_feature_name], number)] = np.mean(
    #     df_X[cont_feature_name][~ops[indicator](df_X[cont_feature_name], number)])
    return df_X


def add_feature_continuous_null(df_X, cont_feature_name):
    """ Adds at most three features (True/False's) to the dataframe where continuous values were null (Ex: -np.inf => column.mean() + "_was_neg_inf"),
        replacing them with the mean. This removes the continuous variables' effects in this region.
        INPUT:
            df_X:
                A dataframe of independent variables.
            cont_feature_name:
                string, the continuous varible to search for null types.
        OUTPUT:
            df_X:
                The same dataframe, with meaned values that were null. At most three new features.
    """
    if (df_X[cont_feature_name] == np.inf).any():
        df_X[cont_feature_name +
             "_was_inf"] = (df_X[cont_feature_name] == np.inf)
        inf_rows = (df_X[cont_feature_name] == np.inf)
        non_inf_rows = (df_X[cont_feature_name] != np.inf)
        df_X.loc[inf_rows, cont_feature_name
                 ] = np.mean(df_X.loc[non_inf_rows, cont_feature_name])

    inf_rows = (df_X[cont_feature_name] == -np.inf)
    if (df_X[cont_feature_name] == -np.inf).any():
        df_X[cont_feature_name +
             "_was_neg_inf"] = (df_X[cont_feature_name] == -np.inf)
        non_inf_rows = (df_X[cont_feature_name] != -np.inf)
        df_X.loc[inf_rows, cont_feature_name
                 ] = np.mean(df_X.loc[non_inf_rows, cont_feature_name])

    if pd.isnull(df_X[cont_feature_name]).any():
        df_X[cont_feature_name +
             "_was_null"] = pd.isnull(df_X[cont_feature_name])
        inf_rows = pd.isnull(df_X[cont_feature_name])
        non_inf_rows = ~pd.isnull(df_X[cont_feature_name])
        df_X.loc[inf_rows, cont_feature_name
                 ] = np.mean(df_X.loc[non_inf_rows, cont_feature_name])
    return df_X


def category_clean_null_and_inf(df_X, cat_feature_name):
    """Finds pesky nulls and np.infs. Replaces them with appropriate strings. (Ex: -np.inf => "was_neg_inf"),
        replacing them with the mean. This removes the continuous variables' effects in this region.
        INPUT:
            df_X:
                A dataframe of independent variables.
            cont_feature_name:
                string, the continuous varible to search for null types.
        OUTPUT:
            df_X:
                The same dataframe, with meaned values that were null. At most three new features (of 0's and 1's).
    """
    df_X.loc[df_X[cat_feature_name] == np.inf, cat_feature_name] = "was_inf"
    df_X.loc[df_X[cat_feature_name] == -np.inf, cat_feature_name] = "was_neg_inf"
    df_X.loc[pd.isnull(df_X[cat_feature_name]), cat_feature_name] = "was_null"
    return df_X

def sort_features(df):
    """Takes a dataframe, returns lists of continuous and categorical features.
    INPUT: dataframe
    OUTPUT: two lists, continuous and categorial features"""
    continuous_features = []
    category_features = []
    for type, feature in zip(df.dtypes, df.dtypes.index):
        if type == np.dtype('int') or type == np.dtype('float'):
            continuous_features.append(feature)
        if (type == np.dtype('O') or
            type == np.dtype('<U') or
            type == np.dtype('bool')):
            category_features.append(feature)
    return (continuous_features, category_features)

def clean_df_X(df_X):
    """ Finds pesky nulls and np.infs. Replaces them with appropriate means or labels. Adds a labeling feature (True/False's only).
        (Ex: -np.inf => "was_neg_inf")
        INPUT:
            df_X:
                A dataframe of independent variables.
        OUTPUT:
            df_X:
                The same dataframe, with meaned values that were null. At most three new features (of 0's and 1's) per column.
    """
    (continuous_features, categorical_features) = sort_features(df_X)
    for feature in continuous_features:
        df_X = add_feature_continuous_null(df_X, feature)
    for feature in categorical_features:
        df_X = category_clean_null_and_inf(df_X, feature)
    for feature in continuous_features:
        if (len(df_X[feature].unique()) <= 1):
            df_X = df_X.drop(feature, axis=1)
    return df_X


def clean_df_respect_to_y(df, y_var_name):
    """ Drops all rows with missing y_var_name.

    INPUT:
        df:
            A dataframe of independent features and one dependent y feature
        y_var_name:
            string, the column name of the dependent y variable in the dataframe
    OUTPUT:
        df:
            A df with no missing y variables
    """
    df = df[df[y_var_name] != np.inf]
    df = df[df[y_var_name] != -np.inf]
    return df[~df[y_var_name].isnull()]


def ints_to_floats(df):
    for type, feature in zip(df.dtypes, df.columns):
        if type == np.dtype('int'):
            df[feature] = df[feature].astype('float')
    return df

def clean_df(df, y_var_name):
    """ Cleans the dataframe. Adds features for nulls, up to three for each continuous variable.
        INPUT:
            df:
                A dataframe of independent features and one dependent y feature
            y_var_name:
                string, the column name of the dependent y variable in the dataframe
        OUTPUT:
            df:
                A cleaned dataframe with correct features added, up to three for each continuous variable.
    """
    df = ints_to_floats(df)
    df = clean_df_respect_to_y(df, y_var_name)
    df_y = df[y_var_name]
    df_X = df.drop(y_var_name, axis=1)
    df_X = clean_df_X(df_X)
    df = df_X
    df[y_var_name] = df_y
    return df


def drop_category_exeeding_limit(df, var_name, category_limit):
    """ Drops category if its # of unique variables exceed the limit.
        INPUT:
            df:
                A dataframe of independent features and one dependent y feature
            var_name:
                string, the column name of the dependent y variable in the dataframe
        OUTPUT:
            df:
                A dataframe with one less feature if it exeeds the limit.
    """
    if len(df[var_name].unique()) > category_limit:
        df.drop(var_name, axis=1)
    return df


def drop_categories_exeeding_limit(df, y_var_name, category_limit):
    """ Drops categories if their # of unique variables exceed the limit.
        INPUT:
            df:
                A dataframe of independent features and one dependent y feature
            y_var_name:
                string, the column name of the dependent y variable in the dataframe
        OUTPUT:
            df:
                A dataframe with X less features for each who exeeds the limit.
    """
    (continuous_features, category_features) = sort_features(
        df.drop(y_var_name, axis=1))
    for cat in category_features:
        if len(df[cat].unique()) > category_limit:
            df.drop(cat, axis=1)
            print('Too many unique values in categorical feature "' +
                  cat + '", dropping "' + cat + '"')
    return df
