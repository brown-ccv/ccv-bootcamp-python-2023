import os
import pandas as pd


def combine_csv_files(path, prefix, suffix='.csv', **kwargs):
    """
    Searches a directory for text files, imports as pandas.DataFrames and
    concatenates to a single DataFrame.

    Args:
        path: pathlib.Path object of a directory
        prefix: String prefix to search for
        suffix: String suffix to search for, Optional, Default '.csv'
        **kwargs: Variable additional arguments pass to the pandas.read_csv function

    Returns: pandas.DataFrame

    """
    # List files in the directory
    list_files_in_path = sorted(os.listdir(path))

    # Initialize an empty list to store DataFrames
    list_df = []

    # Loop through files
    for file in list_files_in_path:
        # Check if the file starts with the prefix and ends with the suffix
        if file.startswith(prefix) and file.endswith(suffix):
            # Read in csv as DataFrame and append it to the list
            list_df.append(pd.read_csv(path / file, **kwargs))
        else:
            continue

    # Concatenate the DataFrames
    df_return = pd.concat(list_df).reset_index(drop=True)

    return df_return
